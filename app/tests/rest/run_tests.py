import unittest
from test_general import General
from intent_test import general_intents_tests
from custom_intent_tests.test_radno_vrijeme import ExtendedRadnoVrijeme
from custom_intent_tests.test_ulaznice import ExtendedUlazniceTest


class IntentTest(unittest.TestCase):
    def test_truthy(self):
        self.assertEqual(True, 1)


def load_tests(loader, standard_tests, pattern):
    suite = unittest.TestSuite()

    for intent_test_case in general_intents_tests:
        suite.addTest(loader.loadTestsFromTestCase(intent_test_case))

    suite.addTest(loader.loadTestsFromTestCase(General))
    suite.addTest(loader.loadTestsFromTestCase(ExtendedRadnoVrijeme))
    suite.addTest(loader.loadTestsFromTestCase(ExtendedUlazniceTest))

    return suite


if __name__ == "__main__":
    unittest.main()
