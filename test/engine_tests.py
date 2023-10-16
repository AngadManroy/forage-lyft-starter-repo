from engine.engine_type.capulet_engine import CapuletEngine
from engine.engine_type.sternman_engine import SternmanEngine
from engine.engine_type.willoughby_engine import WilloughbyEngine
import datetime
import unittest

class Test_Capulet(unittest.TestCase):
    def test_true_capulet(self):
        current_mileage = 50000
        last_service_mileage = 10000
        true_instance = CapuletEngine(current_mileage, last_service_mileage)
        self.assertTrue(true_instance.needs_service())

    def test_false_capulet(self):
        current_mileage = 50000
        last_service_mileage = 40000
        false_instance = CapuletEngine(current_mileage, last_service_mileage)
        self.assertTrue(false_instance.needs_service())

class Test_Willoughby(unittest.TestCase):
    def test_true_willoughby(self):
        current_mileage = 90000
        last_service_mileage = 10000
        true_instance = WilloughbyEngine(current_mileage, last_service_mileage)
        self.assertTrue(true_instance.needs_service())

    def test_false_willoughby(self):
        current_mileage = 50000
        last_service_mileage = 40000
        false_instance = WilloughbyEngine(current_mileage, last_service_mileage)
        self.assertTrue(false_instance.needs_service())

class Test_Sternman(unittest.TestCase):
    def test_true_sternman(self):
        warning = True
        true_instance = SternmanEngine(warning)
        self.assertTrue(true_instance.needs_service())

    def test_false_sternman(self):
        warning = True
        false_instance = SternmanEngine(warning)
        self.assertTrue(false_instance.needs_service())