import unittest
from itertools import product
from lcm import lcm, lcm_naive
from random import randint


class TestLCM(unittest.TestCase):
    def test_small(self):
        for (a, b) in product(range(1, 15), repeat=2):
            self.assertEqual(lcm(a, b), lcm_naive(a, b))

    def test_large(self):
        for (a, b, m) in [(28851538, 1183019, 1933053046), (2*10**9, 2*10**9, 2*10**9), (487543498, 193472147, 94326087313950206)]:
            self.assertEqual(lcm(a, b), m)

    def test_stress(self):
        number_of_iterations = 10
        max_number = 2 * 10**9

        for _ in range(number_of_iterations):
            (a, b) = (randint(1, 2*10**9), randint(1, 2*10**9))
            print(a,b)
            self.assertEqual(lcm(a, b), lcm_naive(a, b))

if __name__ == '__main__':
    unittest.main()
