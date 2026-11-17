# https://github.com/rrathinam203/lab11--RR---HR-
# Partner 1: Rahul Rathinam
# Partner 2: Holly Rockwell

import unittest
import calculator

class TestCalculator(unittest.TestCase):

    def test_add(self):
        self.assertEqual(calculator.add(2, 3), 5)

    def test_divide(self):
        self.assertAlmostEqual(calculator.div(10, 2), 5)

    def test_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            calculator.div(10, 0)

    def test_hypotenuse(self):
        self.assertAlmostEqual(calculator.hypotenuse(3, 4), 5.0)

    def test_log_invalid_argument(self):
        with self.assertRaises(ValueError):
            calculator.logarithm(-5, 10)

    def test_log_invalid_base(self):
        with self.assertRaises(ValueError):
            calculator.logarithm(100, 1)

    def test_logarithm(self):
        self.assertEqual(calculator.logarithm(100, 10), 2.0)

    def test_multiply(self):
        self.assertEqual(calculator.multiply(3, 4), 12)

    def test_sqrt(self):
        self.assertEqual(calculator.square_root(16), 4.0)

    def test_subtract(self):
        self.assertEqual(calculator.subtract(5, 2), 3)

if __name__ == '__main__':
    unittest.main()