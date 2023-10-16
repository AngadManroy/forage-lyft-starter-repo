from tyres.tyre_types.carrigan_tyres import Carrigan_Tyres
from tyres.tyre_types.octoprime_tyres import Octoprime_Tyres
import unittest

class Test_carrigan(unittest.TestCase):
    def test_true_carrigan1(self):
        wear = [0,0,0.2,0.7]
        true_instance = Carrigan_Tyres(wear)
        self.assertTrue(true_instance.needs_service())

    def test_true_carrigan2(self):
        wear = [0,1,0.2,0.7]
        true_instance = Carrigan_Tyres(wear)
        self.assertTrue(true_instance.needs_service())

    def test_false_carrigan1(self):
        wear = [0,0,0,0.7]
        false_instance = Carrigan_Tyres(wear)
        self.assertFalse(false_instance.needs_service())

class Test_octoprime(unittest.TestCase):
    def test_true_octoprime1(self):
        wear = [0.8,0.6,0.9,0.7]
        true_instance = Octoprime_Tyres(wear)
        self.assertTrue(true_instance.needs_service())

    def test_true_octoprime2(self):
        wear = [0.9,1,0.6,1]
        true_instance = Octoprime_Tyres(wear)
        self.assertTrue(true_instance.needs_service())

    def test_false_carrigan1(self):
        wear = [0,0,0,0]
        false_instance = Octoprime_Tyres(wear)
        self.assertFalse(false_instance.needs_service())