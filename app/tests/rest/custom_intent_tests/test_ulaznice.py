from utils.intents import Intent
from intent_test import intent_test_factory


extended_ulaznice = Intent("ulaznice",
                           "Opća ulaznica iznosi 12 €, studenti/umirovljenici 8 €, djeca do 12 g. besplatno.",
                           [
                               "Koliko moram platiti?",
                               "Koliko kosta posjet?",
                               "Ima li popusta?",
                           ])

ExtendedUlazniceTest = intent_test_factory(extended_ulaznice)
