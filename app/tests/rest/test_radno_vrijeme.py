from unittest import TestCase
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
                    primjer[i] = chr(lowercase)
                    typoed_example = "".join(primjer)

                    response = promt_request(typoed_example)
                    assert response.status_code == 200
                    assert response.json()["intent"] == "radno_vrijeme"

                for uppercase in range(ord("A"), ord("Z") + 1):
                    primjer[i] = chr(uppercase)
                    typoed_example = "".join(primjer)

                    response = promt_request(typoed_example)
                    assert response.status_code == 200
                    assert response.json()["intent"] == "radno_vrijeme"

                    primjer[i] = initial_s

                primjer[i] = initial_s
