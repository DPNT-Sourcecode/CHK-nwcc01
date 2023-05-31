import unittest
from lib.solutions.CHK import checkout_solution


class SupermarketCheckOutExercise(unittest.TestCase):
    def test_checkout_method_when_invalid_input_given(self):

        self.assertEqual(checkout_solution.checkout("Invalid String"), -1)


if __name__ == '__main__':
    unittest.main()

