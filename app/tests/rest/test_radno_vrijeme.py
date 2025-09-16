from unittest import TestCase
import threading
import requests

zadani_primjeri = ["Kad radite?", "Koje je radno vrijeme?",
                   "Do kada ste otvoreni danas?"]


def promt_request(message):
    headers = {"X-API-KEY": "TAJNI_KLJUC"}

    json = {
        "message": message
    }

    return requests.post(
        "http://localhost:8000/prompt", headers=headers,
        json=json)


def assert_replaced_char(char, index, message):
    new_message = message[:index] + char + message[index+1:]
    response = promt_request(new_message)
    assert response.status_code == 200
    assert response.json()["intent"] == "radno_vrijeme"


class RadnoVrijeme(TestCase):
    def test_zadani_primjeri_rade(self):
        for n in zadani_primjeri:
            response = promt_request(n)

            assert response.status_code == 200
            assert response.json()["intent"] == "radno_vrijeme"

    def test_modifikacije_zadanih_primjera_rade(self):
        modifikacije_zadanih_primjera = [
            "Od kada do kada radite?", "Koje vam je rano vrijeme?",
            "Do kada ste inace otvoreni?"
        ]

        for n in modifikacije_zadanih_primjera:
            response = promt_request(n)

            assert response.status_code == 200
            assert response.json()["intent"] == "radno_vrijeme"

    # pod typo se misli na malu gresku u jednom slovu
    def test_primjeri_sa_typoom(self):
        for primjer in zadani_primjeri:
            for index in range(len(primjer) - 1):
                threads = []
                for lowercase in range(ord("a"), ord("z") + 1):
                    t1 = threading.Thread(target=assert_replaced_char, args=(
                        chr(lowercase), index, primjer))
                    threads.append(t1)
                    t1.start()

                for uppercase in range(ord("A"), ord("Z") + 1):
                    t2 = threading.Thread(target=assert_replaced_char, args=(
                        chr(uppercase), index, primjer))
                    t2.start()
                    threads.append(t2)

                for t in threads:
                    t.join()
