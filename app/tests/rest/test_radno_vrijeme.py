from unittest import TestCase
import requests

zadani_primjeri = ["Kad radite?", "Koje je rano vrijeme?",
                   "Do kada ste otvoreni danas?"]


class RadnoVrijeme(TestCase):
    # osigurava da zadani primjeri iz zadatka daju dobar odgovor
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
