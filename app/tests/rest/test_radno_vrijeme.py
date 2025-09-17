from unittest import TestCase
import threading
import requests
from app.tests.rest.utils.examples import Examples
from app.tests.rest.utils.synonims import synonims

RadnoVrijemePrimjeri = Examples()
RadnoVrijemePrimjeri.add_example("zadani", [
    "Kad radite?", "Koje je radno vrijeme?",
    "Do kada ste otvoreni danas?"
])

RadnoVrijemePrimjeri.add_example("modificirani", [
    "Od kada do kada radite?", "Koje vam je radno vrijeme?",
    "Do kada ste inace otvoreni?"
])


def promt_request(message):
    headers = {"X-API-KEY": "TAJNI_KLJUC"}

    json = {
        "message": message
    }

    return requests.post(
        "http://localhost:8000/prompt", headers=headers,
        json=json)


class RadnoVrijeme(TestCase):
    def test_zadani__rade(self):
        for n in RadnoVrijemePrimjeri.get_subexample("zadani"):
            response = promt_request(n)

        assert response.status_code == 200
        assert response.json()["intent"] == "radno_vrijeme"

    def test_modifikacije_zadanih_primjera_rade(self):
        for n in RadnoVrijemePrimjeri.get_subexample("modificirani"):
            response = promt_request(n)

            assert response.status_code == 200
            assert response.json()["intent"] == "radno_vrijeme"

    # pod typo se misli na malu gresku u jednom slovu
    def test__sa_typoom(self):
        all_examples = RadnoVrijemePrimjeri.get_all_examples()

        def assert_replaced_char(char, index, message):
            new_message = message[:index] + char + message[index+1:]
            response = promt_request(new_message)
            assert response.status_code == 200
            assert response.json()["intent"] == "radno_vrijeme"

        for primjer in all_examples:
            for index in range(len(all_examples)):
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

    def test__bez_upitnika(self):
        for primjer in RadnoVrijemePrimjeri.get_all_examples():
            response = promt_request(primjer[:-1])
            assert response.status_code == 200
            assert response.json()["intent"] == "radno_vrijeme"

    def test_sa_sinonimima(self):
        for primjer in RadnoVrijemePrimjeri.get_all_examples():
            rijeci = primjer.split(" ")
            for i in range(len(rijeci)):
                rijec = rijeci[i].lower()
                if rijec not in synonims:
                    continue
                for synonim in synonims[rijec]:
                    primjer_sa_sinonimom = " ".join(
                        rijeci[:i] + [synonim] + rijeci[i + 1:])
                    response = promt_request(primjer_sa_sinonimom)
                    assert response.status_code == 200
                    assert response.json()["intent"] == "radno_vrijeme"
