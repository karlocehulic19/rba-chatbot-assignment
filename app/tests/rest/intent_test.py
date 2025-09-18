from unittest import TestCase
from setup import get_all_intents


def intent_test_factory(intent):
    class IntentTest(TestCase):
        def test_existance(self):
            self.assertIsNotNone(intent.type)

    return IntentTest


general_intents_tests = []

for intent in get_all_intents():
    general_intents_tests.append(intent_test_factory(intent))
