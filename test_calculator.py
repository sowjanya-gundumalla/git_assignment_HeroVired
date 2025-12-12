import unittest
from CalculatorPlus import Calculator

class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.c = Calculator()

    def test_add(self):
        self.assertEqual(self.c.add(2, 3), 5)

    def test_divide_by_zero(self):
        with self.assertRaises(ValueError):
            self.c.divide(1, 0)

    def test_sqrt(self):
        self.assertEqual(self.c.square_root(25), 5.0)

if __name__ == "__main__":
    unittest.main()
