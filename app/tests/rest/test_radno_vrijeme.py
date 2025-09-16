from unittest import TestCase
import requests

zadani_primjeri = ["Kad radite?", "Koje je rano vrijeme?",
                   "Do kada ste otvoreni danas?"]

modifikacije_zadanih_primjera = [
    "Od kada do kada radite?", "Koje Vam je rano vrijeme?",
    "Do kada ste inace otvoreni?"
]


class RadnoVrijeme(TestCase):
    def test_zadani_primjeri_rade(self):
        headers = {"X-API-KEY": "TAJNI_KLJUC"}

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
