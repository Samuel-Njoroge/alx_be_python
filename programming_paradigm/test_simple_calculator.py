import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):

    def setUp(self):
        """Set up the SimpleCalculator instance before each test."""
        self.calc = SimpleCalculator()

    def test_addition(self):
        """Test the addition method."""
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertEqual(self.calc.add(3, 4), 7)
        self.assertEqual(self.calc.add(4, 4), 8)
        self.assertEqual(self.calc.add(5, 4), 9)

    def test_subtraction(self):
        """Test the subtraction method."""
        self.assertEqual(self.calc.subtract(3, 3), 0)
        self.assertEqual(self.calc.subtract(-1, 1), -2)
        self.assertEqual(self.calc.subtract(7, 2), 5)
        self.assertEqual(self.calc.subtract(6, 4), 2)
        self.assertEqual(self.calc.subtract(8, 5), 3)

    def test_multiplication(self):
        """Test the multiplication method."""
        self.assertEqual(self.calc.multiply(2, 3), 6)
        self.assertEqual(self.calc.multiply(-1, 1), -1)
        self.assertEqual(self.calc.multiply(3, 4), 12)
        self.assertEqual(self.calc.multiply(4, 4), 16)
        self.assertEqual(self.calc.multiply(5, 4), 20)

    def test_division(self):
        """Test the division method."""
        self.assertEqual(self.calc.divide(15, 3), 5)
        self.assertEqual(self.calc.divide(8, 2), 4)
        self.assertEqual(self.calc.divide(6, 3), 2)
        self.assertEqual(self.calc.divide(0, 4), 0)
        self.assertIsNone(self.calc.divide(5, 0))

    def test_divide_float_precision(self):
        self.assertAlmostEqual(self.calc.divide(1, 3), 1/3)
        self.assertAlmostEqual(self.calc.divide(22, 7), 22/7)