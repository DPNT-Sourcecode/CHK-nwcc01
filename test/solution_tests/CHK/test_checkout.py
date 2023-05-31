import unittest
from lib.solutions.CHK import checkout_solution


class SupermarketCheckOutExercise(unittest.TestCase):
    def test_returns_minus_one_when_invalid_string_is_given(self):

        self.assertEqual(checkout_solution.checkout("Invalid String"), -1)

    def test_checkout_method_returns_minus_one_when_invalid_characters_part_of_string(self):
        test_string = "ABCxD"
        self.assertEqual(checkout_solution.checkout(test_string), -1)

    def test_checkout_method_returns_correct_calculation_for_one_of_each_item(self):
        test_string = "ABCD"
        self.assertEqual(checkout_solution.checkout(test_string), 115)


if __name__ == '__main__':
    unittest.main()


