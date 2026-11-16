# https://github.com/rrathinam203/lab11--RR---HR-
# Partner 1: Rahul Rathinam
# Partner 2: Holly Rockwell

import unittest
import calculator

class TestCalculator(unittest.TestCase):

    def test_multiply(self):
        self.assertEqual(calculator.mul(3, 4), 12)
        self.assertEqual(calculator.mul(-2, 5), -10)
        self.assertEqual(calculator.mul(0, 100), 0)

    def test_divide(self):
        self.assertAlmostEqual(calculator.divide(2, 10), 5.0)
        self.assertAlmostEqual(calculator.divide(4, -8), -2.0)
        with self.assertRaises(ZeroDivisionError):
            calculator.divide(0, 10)

    def test_log_invalid_argument(self):
        with self.assertRaises(ValueError):
            calculator.logarithm(-2, 10)
        with self.assertRaises(ValueError):
            calculator.logarithm(1, 10)
        with self.assertRaises(ValueError):
            calculator.logarithm(10, -5)
        with self.assertRaises(ValueError):
            calculator.logarithm(10, 0)

    def test_hypotenuse(self):
        self.assertAlmostEqual(calculator.hypotenuse(3, 4), 5.0)
        self.assertAlmostEqual(calculator.hypotenuse(-5, 12), 13.0)
        self.assertAlmostEqual(calculator.hypotenuse(0, 0), 0.0)

    def test_sqrt(self):
        self.assertAlmostEqual(calculator.square_root(16), 4.0)
        self.assertAlmostEqual(calculator.square_root(0), 0.0)
        with self.assertRaises(ValueError):
            calculator.square_root(-9)

if __name__ == '__main__':
    unittest.main()

