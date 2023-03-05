import unittest
import engine as eg

class TestCapuletEngine(unittest.TestCase):
    def test_needs_service_true(self):
        current_mileage = 120000
        last_service_mileage = 50000
        engine = eg.CapuletEngine(current_mileage, last_service_mileage)
        self.assertTrue(engine.engine_needs_service())

    def test_needs_service_false(self):
        current_mileage = 30000
        last_service_mileage = 0
        engine = eg.CapuletEngine(current_mileage, last_service_mileage)
        self.assertFalse(engine.engine_needs_service())

class TestWilloughbyEngine(unittest.TestCase):
    def test_needs_service_true(self):
        current_mileage = 91200
        last_service_mileage = 30000
        engine = eg.WilloughbyEngine(current_mileage, last_service_mileage)
        self.assertTrue(engine.engine_needs_service())

    def test_needs_service_false(self):
        current_mileage = 60000
        last_service_mileage = 0
        engine = eg.WilloughbyEngine(current_mileage, last_service_mileage)
        self.assertFalse(engine.engine_needs_service())

class TestSternmanEngine(unittest.TestCase):
    def test_needs_service_true(self):
        warning_light_is_on = True
        engine = eg.SternmanEngine(warning_light_is_on)
        self.assertTrue(engine.engine_needs_service())

    def test_needs_service_false(self):
        warning_light_is_on = False
        engine = eg.SternmanEngine(warning_light_is_on)
        self.assertFalse(engine.engine_needs_service())


