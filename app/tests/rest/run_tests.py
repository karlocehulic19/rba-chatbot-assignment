import unittest
from test_general import General
from test_radno_vrijeme import RadnoVrijeme
from intent_test import general_intents_tests


class IntentTest(unittest.TestCase):
    def test_truthy(self):
        self.assertEqual(True, 1)


def load_tests(loader, standard_tests, pattern):
    suite = unittest.TestSuite()

    for intent_test_case in general_intents_tests:
        suite.addTest(loader.loadTestsFromTestCase(intent_test_case))

    suite.addTest(loader.loadTestsFromTestCase(General))
    suite.addTest(loader.loadTestsFromTestCase(RadnoVrijeme))

    return suite


if __name__ == "__main__":
    unittest.main()
