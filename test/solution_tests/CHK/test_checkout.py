import unittest
from lib.solutions.CHK import checkout_solution


class SupermarketCheckOutExercise(unittest.TestCase):
    def test_checkout_method(self):

        self.assertEqual(checkout_solution.checkout(5), 10)


if __name__ == '__main__':
    unittest.main()

