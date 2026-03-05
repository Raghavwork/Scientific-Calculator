import unittest
from calculator import square_root, factorial, natural_log, power

class TestCalculator(unittest.TestCase):

    def test_sqrt(self):
        self.assertEqual(square_root(16), 4)

    def test_factorial(self):
        self.assertEqual(factorial(5), 120)

    def test_ln(self):
        self.assertAlmostEqual(natural_log(1), 0)

    def test_power(self):
        self.assertEqual(power(2,3), 8)

if __name__ == '__main__':
    unittest.main()
