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

    def test_the_deal_price_for_item_a_works(self):
        test_string = "AAA"
        self.assertEqual(130, checkout_solution.checkout(test_string))

    def test_the_deal_price_for_item_b_works(self):
        test_string = "BB"
        self.assertEqual(45, checkout_solution.checkout(test_string))

    def test_returns_200_for_the_five_item_a_deal_price(self):
        test_string = "AAAAA"
        self.assertEqual(200, checkout_solution.checkout(test_string))

    def test_a_more_complicated_order(self):
        test_string = "ABCDCBAABCABBAAA"
        # 7As, 5Bs, 3Cs, 1D
        # 300, 120, 60, 15
        self.assertEqual(sum([300, 120, 60, 15]), checkout_solution.checkout(test_string))

    def test_more_bs_are_added_when_atleast_2_es_are_bought(self):
        test_string = "ABCDEE"
        # 50, 45, 20, 15, 80
        self.assertEqual(sum([50, 45, 20, 15, 80]), checkout_solution.checkout(test_string))

    def test_stuff(self):
        test_string = "EEEB"
        # 50, 45, 20, 15, 80
        self.assertEqual(120, checkout_solution.checkout(test_string))


if __name__ == '__main__':
    unittest.main()


"""
Some requests have failed (9/40). Here are some of them:
 - {"method":"checkout","params":["EE"],"id":"CHK_R2_023"}, expected: 80, got: 110
 - {"method":"checkout","params":["EEB"],"id":"CHK_R2_024"}, expected: 80, got: 125
 - {"method":"checkout","params":["EEEB"],"id":"CHK_R2_025"}, expected: 120, got: 165
 """



