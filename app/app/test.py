"""
Sample tests
"""

from django.test import SimpleTestCase
from app import calc


class CalcTests(SimpleTestCase):
    # Test Calc module

    def test_add_numbers(self):
        # Test adding numbers together
        res = calc.add(5, 6)
        self.assertEqual(res, 11)

    def test_subtract_numbers(self):
        # subtracting numbers test
        res = calc.subtract(10, 15)
        self.assertEqual(res, 5)
