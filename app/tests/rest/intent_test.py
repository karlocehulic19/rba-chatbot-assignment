from unittest import TestCase
from setup import get_all_intents
import requests
import threading

from utils.examples import Examples
from utils.keyboard import CroatianKeyboard
from utils.keyboard import CroatianUppercaseKeyboard


def promt_request(message):
    headers = {"X-API-KEY": "TAJNI_KLJUC"}

    json = {
        "message": message
    }

    return requests.post(
        "http://localhost:8000/prompt", headers=headers,
        json=json)


def intent_test_factory(intent):
    def assert_right_intent(test, response):
        json = response.json()

        test.assertEqual(response.status_code, 200)
        test.assertEqual(json["intent"], intent.type)

    class IntentTest(TestCase):
        def test_zadani_rade(self):
            for n in intent.examples.get_subexample(Examples.DEFAULT_SUBTYPE):
                response = promt_request(n)
                assert_right_intent(self, response)

        # pod typo se misli na malu gresku u jednom slovu
        def test__sa_typoom(self):
            all_examples = intent.examples.get_all_examples()

            def assert_replaced_char(char, index, message):
                if not char:
                    print("NOT CHAR")

                new_message = message[:index] + char + message[index+1:]
                response = promt_request(new_message)
                assert_right_intent(self, response)

            for primjer in all_examples:
                for index in range(len(primjer)):
                    threads = []
                    curr_char = primjer[index]

                    for nei in CroatianUppercaseKeyboard.get_neighbors(
                            curr_char):
                        t1 = threading.Thread(
                            target=assert_replaced_char, args=(nei, index,
                                                               primjer))
                        threads.append(t1)
                        t1.start()

                    for nei in CroatianKeyboard.get_neighbors(curr_char):
                        t2 = threading.Thread(target=assert_replaced_char,
                                              args=(nei, index, primjer))
                        threads.append(t1)
                        t2.start()

                    for t in threads:
                        t.join()

        def test_bez_upitnika(self):
            for primjer in intent.examples.get_all_examples():
                response = promt_request(primjer[:-1])
                assert_right_intent(self, response)

        def test_sa_sinonimima(self):
            for synonim_primjeri in intent.examples.get_all_synonims():
                response = promt_request(synonim_primjeri)
                assert_right_intent(self, response)

    return IntentTest


general_intents_tests = []

for intent in get_all_intents():
    general_intents_tests.append(intent_test_factory(intent))
