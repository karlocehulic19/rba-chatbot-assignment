from utils.intents import Intent
from intent_test import intent_test_factory


extended_danas_izlozbe = Intent("danas_izlozbe",
                                "Današnji naglasci: 'Impresionisti Save' i 'Stari obrti Slavonije'.",
                                [
                                    "Što cu danas vidjeti?",
                                ])

ExtendedDanasIzlozbe = intent_test_factory(extended_danas_izlozbe)
