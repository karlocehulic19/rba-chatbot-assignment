from utils.intents import Intent
from intent_test import intent_test_factory


extended_adresa = Intent("adresa",
                         "Gradski Muzej Rivertown, Riječka avenija 12, Zagreb.",
                         [
                             "Gdje vas mogu naci?",
                             "Gdje trebam doci?",
                         ])

ExtendedAdresaTest = intent_test_factory(extended_adresa)
