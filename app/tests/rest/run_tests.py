import unittest
from test_general import General
from test_radno_vrijeme import RadnoVrijeme


class IntentTest(unittest.TestCase):
    def test_truthy(self):
        self.assertEqual(True, 1)


if __name__ == "__main__":
    unittest.main()
