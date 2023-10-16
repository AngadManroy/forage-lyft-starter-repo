from battery.battery_type.nubbin_battery import Nubbin_battery
from battery.battery_type.spindler_battery import Spindler_battery

import unittest
import datetime

class Test_nubbin(unittest.TestCase):
    def test_true_nubbin(self):
        current_date = datetime.datetime(2023,10,16)
        last_service_date = datetime.datetime(2020,10,16)
        true_instance = Nubbin_battery(current_date, last_service_date)
        self.assertTrue(true_instance.needs_service())

    def test_false_nubbin(self):
        current_date = datetime.datetime(2023,10,16)
        last_service_date = datetime.datetime(2022,10,16)
        false_instance = Nubbin_battery(current_date, last_service_date)
        self.assertFalse(false_instance.needs_service())

class Test_spindler(unittest.TestCase):
    def test_true_spindler(self):
        current_date = datetime.datetime(2023,10,16)
        last_service_date = datetime.datetime(2017,10,16)
        true_instance = Spindler_battery(current_date, last_service_date)
        self.assertTrue(true_instance.needs_service())

    def test_false_spindler(self):
        current_date = datetime.datetime(2023,10,16)
        last_service_date = datetime.datetime(2022,10,16)
        false_instance = Spindler_battery(current_date, last_service_date)
        self.assertFalse(false_instance.needs_service())