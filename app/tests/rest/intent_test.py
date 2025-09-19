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
    def assert_right_intent(test, response, question):
        json = response.json()

        test.assertEqual(response.status_code, 200)
        test.assertEqual(json["intent"], intent.type,
                         f"Intent type missaligment: should be \"{intent.type}\" \
but is \"{json['intent']}\" \n For question: {question}")

        probs = json["probs"]
        max_prob = max(probs, key=lambda x: probs[x])

        test.assertEqual(probs[intent.type], probs[max_prob], f"Probs inccorect pick, should be \"{intent.type}\": {probs[intent.type]} \n \
but is \"f{max_prob}\": {probs[max_prob]}")

    class IntentTest(TestCase):
        def test_zadani_rade(self):
            for n in intent.examples.get_subexample(Examples.DEFAULT_SUBTYPE):
                response = promt_request(n)
                assert_right_intent(self, response, n)

        # pod typo se misli na malu gresku u jednom slovu
        def test_sa_typoom(self):
            all_examples = intent.examples.get_all_examples()

            def assert_replaced_char(char, index, message):
                new_message = message[:index] + char + message[index+1:]
                response = promt_request(new_message)
                assert_right_intent(self, response, new_message)

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
                assert_right_intent(self, response, primjer[:-1])

        def test_sa_sinonimima(self):
            for synonim_primjeri in intent.examples.get_all_synonims():
                response = promt_request(synonim_primjeri)
                assert_right_intent(self, response, synonim_primjeri)

        def test_sve_umanjeno(self):
            for primjer in intent.examples.get_all_examples():
                lowered = primjer.lower()
                response = promt_request(primjer.lower())
                assert_right_intent(self, response, lowered)

        def test_sve_uvecano(self):
            for primjer in intent.examples.get_all_examples():
                uppered = primjer.upper()
                response = promt_request(uppered)
                assert_right_intent(self, response, uppered)

    return IntentTest


general_intents_tests = []

for intent in get_all_intents():
    general_intents_tests.append(intent_test_factory(intent))
