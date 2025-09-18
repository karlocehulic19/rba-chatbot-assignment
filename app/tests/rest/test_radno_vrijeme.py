from unittest import TestCase
import threading
import requests
import unittest
from utils.examples import Examples
from utils.keyboard import CroatianKeyboard
from utils.keyboard import CroatianUppercaseKeyboard

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


def assert_radno_vrimjeme(response):
    assert response.status_code == 200
    assert response.json()["intent"] == "radno_vrijeme"


class RadnoVrijeme(TestCase):
    def test_zadani__rade(self):
        for n in RadnoVrijemePrimjeri.get_subexample("zadani"):
            response = promt_request(n)
            assert_radno_vrimjeme(response)

    def test_modifikacije_zadanih_primjera_rade(self):
        for n in RadnoVrijemePrimjeri.get_subexample("modificirani"):
            response = promt_request(n)
            assert_radno_vrimjeme(response)

    # pod typo se misli na malu gresku u jednom slovu
    def test__sa_typoom(self):
        all_examples = RadnoVrijemePrimjeri.get_all_examples()

        def assert_replaced_char(char, index, message):
            new_message = message[:index] + char + message[index+1:]
            response = promt_request(new_message)
            assert_radno_vrimjeme(response)

        for primjer in all_examples:
            for index in range(len(primjer)):
                threads = []
                curr_char = primjer[index]

                if curr_char.isupper():
                    for nei in CroatianUppercaseKeyboard.get_neighbors(
                            curr_char):
                        t1 = threading.Thread(
                            target=assert_replaced_char, args=(nei, index,
                                                               primjer))
                        threads.append(t1)
                        t1.start()
                else:
                    for nei in CroatianKeyboard.get_neighbors(curr_char):
                        t2 = threading.Thread(target=assert_replaced_char,
                                              args=(nei, index, primjer))
                        threads.append(t1)
                        t2.start()

                for t in threads:
                    t.join()

    def test_bez_upitnika(self):
        for primjer in RadnoVrijemePrimjeri.get_all_examples():
            response = promt_request(primjer[:-1])
            assert_radno_vrimjeme(response)

    def test_sa_sinonimima(self):
        for synonim_primjeri in RadnoVrijemePrimjeri.get_all_synonims():
            response = promt_request(synonim_primjeri)
            assert_radno_vrimjeme(response)
