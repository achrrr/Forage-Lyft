import unittest
from datetime import datetime
import battery as bt

class TestNubbinBattery(unittest.TestCase):
    def test_needs_service_true(self):
        current_date = datetime.fromisoformat("2023-07-20")
        last_service_date = datetime.fromisoformat("2019-01-20")
        battery = bt.NubbinBattery(current_date, last_service_date)
        self.assertTrue(battery.battery_needs_service())

    def test_needs_service_false(self):
        current_date = datetime.fromisoformat("2023-05-15")
        last_service_date = datetime.fromisoformat("2022-01-10")
        battery = bt.NubbinBattery(current_date, last_service_date)
        self.assertFalse(battery.battery_needs_service())

class TestSpindlerBattery(unittest.TestCase):
    def test_needs_service_true(self):
        current_date = datetime.fromisoformat("2021-06-15")
        last_service_date = datetime.fromisoformat("2018-01-05")
        battery = bt.SpindlerBattery(current_date, last_service_date)
        self.assertTrue(battery.battery_needs_service())

    def test_needs_service_false(self):
        current_date = datetime.fromisoformat("2020-08-15")
        last_service_date = datetime.fromisoformat("2019-01-10")
        battery = bt.SpindlerBattery(current_date, last_service_date)
        self.assertFalse(battery.battery_needs_service())