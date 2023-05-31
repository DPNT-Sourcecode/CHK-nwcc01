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

    def test_more_bs_are_removed_when_atleast_2_es_are_bought(self):
        test_string = "ABCDEE"
        # 50, 45, 20, 15, 80
        self.assertEqual(sum([50, 20, 15, 80]), checkout_solution.checkout(test_string))

    def test_multiple_es(self):
        test_string = "EEEB"
        self.assertEqual(120, checkout_solution.checkout(test_string))

        test_string = "EEB"
        self.assertEqual(80, checkout_solution.checkout(test_string))

        test_string = "EE"
        # 50, 45, 20, 15, 80
        self.assertEqual(80, checkout_solution.checkout(test_string))

    def test_when_five_f_items_are_bought_only_three_are_paid_for(self):
        test_string = "FFFFF"
        self.assertEqual(40, checkout_solution.checkout(test_string))

    def test_when_seven_f_items_are_bought_only_five_are_paid_for(self):
        test_string = "FFFFFFF"
        self.assertEqual(50, checkout_solution.checkout(test_string))

    def test_when_two_f_items_are_bought_two_are_paid_for(self):
        test_string = "FF"
        self.assertEqual(20, checkout_solution.checkout(test_string))

    def test_five_hs_returns_45(self):
        test_string = "HHHHH"
        self.assertEqual(45, checkout_solution.checkout(test_string))

    def test_ten_hs_returns_80(self):
        test_string = "HHHHHHHHHH"
        self.assertEqual(80, checkout_solution.checkout(test_string))

    def test_two_ks_returns_150(self):
        test_string = "KK"
        self.assertEqual(150, checkout_solution.checkout(test_string))

    def test_three_ns_returns_120(self):
        test_string = "NNN"
        self.assertEqual(120, checkout_solution.checkout(test_string))

    def test_three_ns_and_one_n_returns_120(self):
        test_string = "MNNN"
        self.assertEqual(120, checkout_solution.checkout(test_string))

    def test_5_ps_returns_200(self):
        test_string = "PPPPP"
        self.assertEqual(200, checkout_solution.checkout(test_string))

    def test_three_qs_returns_80(self):
        test_string = "QQQ"
        self.assertEqual(80, checkout_solution.checkout(test_string))

    def test_multiple_rs_and_qs_return_the_right_value(self):
        test_string = "RRRQ"
        self.assertEqual(150, checkout_solution.checkout(test_string))

        test_string = "RRRQQ"
        self.assertEqual(180, checkout_solution.checkout(test_string))

        test_string = "RRRQQQ"
        self.assertEqual(210, checkout_solution.checkout(test_string))

    def test_four_us_returns_120(self):
        test_string = "UUUU"
        self.assertEqual(120, checkout_solution.checkout(test_string))

    def test_two_vs_return_90(self):
        test_string = "VV"
        self.assertEqual(90, checkout_solution.checkout(test_string))

    def test_three_vs_return_130(self):
        test_string = "VVV"
        self.assertEqual(130, checkout_solution.checkout(test_string))

    def test_three_ss_return_45(self):
        test_string = "SSS"
        self.assertEqual(45, checkout_solution.checkout(test_string))

    def test_two_ss_and_a_t_returns_45(self):
        test_string = "SST"
        self.assertEqual(45, checkout_solution.checkout(test_string))

    def test_two_zs_and_two_xs_returns_62(self):
        test_string = "ZZXX"
        self.assertEqual(62, checkout_solution.checkout(test_string))

    def test_lots_of_deal_items_return_the_correct_amount(self):
        test_string = "ZZXXSTZT"
        self.assertEqual(124, checkout_solution.checkout(test_string))

        test_string = "ZZXXSTZTYY"
        self.assertEqual(124, checkout_solution.checkout(test_string))


if __name__ == '__main__':
    unittest.main()

   #  - {"method": "checkout", "params": ["NNN"], "id": "CHK_R4_105"}, expected: 120, got: 105



