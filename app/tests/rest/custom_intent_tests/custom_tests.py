from .test_radno_vrijeme import ExtendedRadnoVrijeme
from .test_adresa import ExtendedAdresaTest
from .test_ulaznice import ExtendedUlazniceTest
from .test_danas_izlozbe import ExtendedDanasIzlozbe
from .test_kafic import ExtendedKaficTest


custom_tests = [
    ExtendedRadnoVrijeme,
    ExtendedAdresaTest,
    ExtendedUlazniceTest,
    ExtendedDanasIzlozbe,
    ExtendedKaficTest
]
