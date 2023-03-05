import unittest
from datetime import datetime
from tires import Carrigan as cr
from tires import Octoprime as op

class TestCarrigan(unittest.TestCase):

    def test_tires_should_be_replaced(self):

        tire_data = [0,0,1,0]
        tire = cr.Carrigan(tire_data)

        self.assertTrue(tire.needs_service())
    
    def test_tires_should_not_be_replaced(self):

        tire_data = [0,0.5,0.7,0]
        tire = cr.Carrigan(tire_data)

        self.assertFalse(tire.needs_service())

class TestOctoprime(unittest.TestCase):

    def test_tires_should_not_be_replaced(self):

        tire_data = [1, 1, 0.5, 0]
        tire = op.Octoprime(tire_data)

        self.assertFalse(tire.needs_service())
    
    def test_tires_should_be_replaced(self):

        tire_data = [1,2,3,0]
        tire = op.Octoprime(tire_data)
        self.assertTrue(tire.needs_service())
