import unittest
from gcd import gcd, gcd_naive


class TestGCD(unittest.TestCase):
    def test_small(self):
        for (a, b) in [(1, 1), (2, 6), (7, 1), (1, 13), (2, 19), (15, 5), (37, 23)]:
            self.assertEqual(gcd(a, b), gcd_naive(a, b))

    def test_large(self):
        for (a, b, d) in [(28851538, 1183019, 17657), (999999999, 2*10**9, 1), (2*10**9, 2*10**9, 2*10**9), (379379475, 94294569, 3)]:
            self.assertEqual(gcd(a, b), d)


if __name__ == '__main__':
    unittest.main()
