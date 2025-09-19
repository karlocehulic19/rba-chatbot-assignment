from utils.intents import Intent
from intent_test import intent_test_factory


extended_kafic = Intent("kafic",
                        "Kafić Riverbend u prizemlju nudi grickalice, kavu i čaj.",
                        [
                            "Mogu li sto popiti?",
                            "Mogu li sto pojesti?",
                        ])

ExtendedKaficTest = intent_test_factory(extended_kafic)
