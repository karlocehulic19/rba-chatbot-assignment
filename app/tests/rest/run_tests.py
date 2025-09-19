import unittest
from test_general import General
from intent_test import general_intents_tests
from custom_intent_tests.custom_tests import custom_tests


class IntentTest(unittest.TestCase):
    def test_truthy(self):
        self.assertEqual(True, 1)


def load_tests(loader, standard_tests, pattern):
    suite = unittest.TestSuite()
    suite.addTest(loader.loadTestsFromTestCase(General))

    for intent_test_case in general_intents_tests:
        suite.addTest(loader.loadTestsFromTestCase(intent_test_case))

    for custom_intent_test in custom_tests:
        suite.addTest(loader.loadTestsFromTestCase(custom_intent_test))

    return suite


if __name__ == "__main__":
    unittest.main()
