from unittest import TestCase
import requests

zadani_primjeri = ["Kad radite?", "Koje je radno vrijeme?",
                   "Do kada ste otvoreni danas?"]


headers = {"X-API-KEY": "TAJNI_KLJUC"}


class RadnoVrijeme(TestCase):
    def test_zadani_primjeri_rade(self):
        for n in zadani_primjeri:
            json = {
                "message": n
            }

            response = requests.post(
                "http://localhost:8000/prompt", headers=headers, json=json)

            assert response.status_code == 200
            assert response.json()["intent"] == "radno_vrijeme"

    def test_modifikacije_zadanih_primjera_rade(self):
        modifikacije_zadanih_primjera = [
            "Od kada do kada radite?", "Koje vam je rano vrijeme?",
            "Do kada ste inace otvoreni?"
        ]

        for n in modifikacije_zadanih_primjera:
            json = {
                "message": n
            }

            response = requests.post(
                "http://localhost:8000/prompt", headers=headers, json=json)

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
