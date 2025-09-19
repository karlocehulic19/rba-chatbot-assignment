from utils.intents import Intent
from intent_test import intent_test_factory


extended_radno_vrijeme = Intent("radno_vrijeme",
                                "Otvoreni smo uto–ned 10:00–18:00. Ponedjeljkom zatvoreno.",
                                [
                                    "Do kad radite?",
                                    "Od kad radite?",
                                    "Kad mogu doci?",
                                ])

ExtendedRadnoVrijeme = intent_test_factory(extended_radno_vrijeme)
