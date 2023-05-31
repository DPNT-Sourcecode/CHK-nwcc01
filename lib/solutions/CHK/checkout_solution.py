import math
from typing import Union

# noinspection PyUnusedLocal
# skus = unicode string

""" Items which have deals that don't affect others"""
# A, B, F, H, K, P, Q, U, V

""" Items with deals that do affect others """
# E, N, R#

""" Items with single deals """
# B, K, P, Q

"""Items with no deals"""
# C, D, G, I, J, L, M, O, S, T, W, X, Y, Z


def checkout(skus: str) -> int:
    supermarket_item_dict = parse_string(skus)

    # invalid string return -1
    if supermarket_item_dict == -1:
        return -1

    easy_ones_total = 0
    simple_deal_total = 0
    free_deal_1_total = 0
    free_deal_2_total = 0
    for product_name in supermarket_item_dict:
        if supermarket_item_dict[product_name][2] == "free deal 1":
            data = supermarket_item_dict.get(product_name)
            product_price = data[1]
            quantity = data[0]
            free_product_name = data[3][1]
            deal_quantity = data[3][0]
            returned_data = other_item_free_deal_calculation(quantity, deal_quantity, product_price)
            free_deal_1_total += returned_data[0]
            quantity_of_free_items = returned_data[1]
            supermarket_item_dict[free_product_name][0] -= quantity_of_free_items

        elif supermarket_item_dict[product_name][2] == "single":
            data = supermarket_item_dict.get(product_name)
            product_price = data[1]
            quantity = data[0]
            easy_ones_total += simple_price_calculation(product_price, quantity)

        elif supermarket_item_dict[product_name][2] == "simple deal":
            data = supermarket_item_dict.get(product_name)
            product_price = data[1]
            quantity = data[0]
            deal_price = data[3][1]
            deal_quantity = data[3][0]

            simple_deal_total += single_deal_calculation(product_price, deal_price, deal_quantity, quantity)

        elif supermarket_item_dict[product_name][2] == "free deal 2":
            data = supermarket_item_dict.get(product_name)
            product_price = data[1]
            quantity = data[0]
            deal_quantity = data[3]
            free_deal_2_total += same_item_free_deal_calculation(quantity, deal_quantity, product_price)

    total_cost_a = calculate_cost_of_a_item(supermarket_item_dict)

    # total_cost_c = calculate_cost_c_item(supermarket_item_dict)
    #
    # total_cost_d = calculate_cost_d_item(supermarket_item_dict)

    # total_cost_e = calculate_cost_e_item(supermarket_item_dict)[0]
    # number_of_bs_free = calculate_cost_e_item(supermarket_item_dict)[1]
    #
    # supermarket_item_dict["B"][0] -= number_of_bs_free
    # total_cost_b = calculate_cost_of_b_item(supermarket_item_dict)

    # total_cost_f = calculate_cost_f_item(supermarket_item_dict)

    total_cost = total_cost_a + simple_deal_total + easy_ones_total + free_deal_1_total + free_deal_2_total

    return total_cost


def parse_string(skus: str) -> Union[int, dict]:
    """ Store number of each item in a dictionary"""
    supermarket_item_dict = {
        "E": [0, 40, "free deal 1", [2, "B"]],
        "N": [0, 40, "free deal 1", [3, "M"]],
        "R": [0, 50, "free deal 1", [3, "Q"]],
        "A": [0, 50, "deal"],
        "B": [0, 30, "simple deal", [2, 45]],
        "C": [0, 20, "single"],
        "D": [0, 15, "single"],
        "F": [0, 10, "free deal 2", 3],
        "G": [0, 20, "single"],
        "H": [0, 10, "deal"],
        "I": [0, 35, "single"],
        "J": [0, 60, "single"],
        "K": [0, 80, "simple deal", [2, 150]],
        "L": [0, 90, "single"],
        "M": [0, 15, "single"],
        "O": [0, 10, "single"],
        "P": [0, 50, "simple deal", [5, 200]],
        "Q": [0, 30, "simple deal", [3, 80]],
        "S": [0, 30, "single"],
        "T": [0, 20, "single"],
        "U": [0, 40, "free deal 2", 4],
        "V": [0, 50, "deal"],
        "W": [0, 20, "single"],
        "X": [0, 90, "single"],
        "Y": [0, 10, "single"],
        "Z": [0, 50, "single"]

    }
    # loop through the string to determine how many of each item is required and return -1 if an invalid input is given
    for char in skus:
        quantity = supermarket_item_dict.get(char, None)
        if quantity is None:
            return -1
        else:
            supermarket_item_dict[char][0] += 1

    return supermarket_item_dict


def calculate_cost_of_a_item(supermarket_item_dict: dict) -> int:
    quantity_a = supermarket_item_dict["A"][0]
    cost_a_single = 50
    bulk_price_a_three = 130
    bulk_quantity_a_three = 3
    bulk_quantity_a_five = 5
    bulk_price_a_five = 200

    # check if there is more than 2 a items bought to calculate deal price
    if 2 < quantity_a < bulk_quantity_a_five:
        if quantity_a % bulk_quantity_a_three == 0:
            # they have bought a multiple 3 amount of item A
            total_cost_a = (quantity_a / bulk_quantity_a_three) * bulk_price_a_three

        else:
            total_cost_a = (math.floor(quantity_a / bulk_quantity_a_three) * bulk_price_a_three) \
                           + ((quantity_a % bulk_quantity_a_three) * cost_a_single)
    # check if they have bought a multiple of 5
    elif quantity_a >= bulk_quantity_a_five:
        # check if exactly divisible by 5
        if quantity_a % bulk_quantity_a_five == 0:
            total_cost_a = (quantity_a / bulk_quantity_a_five) * bulk_price_a_five
        else:
            # check the remainder is not a multiple of 3
            remainder = quantity_a % bulk_quantity_a_five
            if remainder >= bulk_quantity_a_three:
                single_purchases = remainder - bulk_quantity_a_three
                total_cost_a = (math.floor(quantity_a / bulk_quantity_a_five) * bulk_price_a_five) \
                                + bulk_price_a_three + (single_purchases * cost_a_single)
            else:
                total_cost_a = (math.floor(quantity_a / bulk_quantity_a_five) * bulk_price_a_five) \
                               + (remainder * cost_a_single)
    else:
        total_cost_a = quantity_a * cost_a_single

    return total_cost_a


def calculate_cost_of_b_item(supermarket_item_dict: dict) -> int:
    quantity_b = supermarket_item_dict["B"][0]
    cost_b_single = 30
    bulk_price_b = 45
    bulk_quantity_b = 2

    # check if there is more than 1 B items bought to calculate deal price
    if quantity_b > 1:
        if quantity_b % bulk_quantity_b == 0:
            # they have bought a multiple 2 amount of item B
            total_cost_b = (quantity_b / bulk_quantity_b) * bulk_price_b

        else:
            total_cost_b = (math.floor(quantity_b / bulk_quantity_b) * bulk_price_b) \
                           + ((quantity_b % bulk_quantity_b) * cost_b_single)
    elif quantity_b < 0:
        total_cost_b = 0
        return total_cost_b
    else:
        total_cost_b = quantity_b * cost_b_single

    return total_cost_b


def calculate_cost_c_item(supermarket_item_dict: dict) -> int:
    quantity_c = supermarket_item_dict["C"][0]
    cost_c_single = supermarket_item_dict["C"][1]

    total_cost_c = quantity_c * cost_c_single

    return total_cost_c


def calculate_cost_d_item(supermarket_item_dict: dict) -> int:
    quantity_d = supermarket_item_dict["D"][0]
    cost_d_single = 15
    total_cost_d = quantity_d * cost_d_single

    return total_cost_d


def calculate_cost_e_item(supermarket_item_dict: dict) -> tuple:
    quantity_e = supermarket_item_dict["E"][0]
    cost_e_single = 40
    bulk_quantity_item_b = 2

    number_of_bs_free = math.floor(quantity_e / bulk_quantity_item_b)
    total_cost_e = quantity_e * cost_e_single

    return total_cost_e, number_of_bs_free


def calculate_cost_f_item(supermarket_item_dict: dict) -> int:
    quantity_f = supermarket_item_dict["F"][0]
    cost_f_single = 10
    bulk_quantity = 3

    if quantity_f >= bulk_quantity:
        quantity_of_free_f_items = math.floor(quantity_f / bulk_quantity)
        f_items_to_pay_for = quantity_f - quantity_of_free_f_items
        total_cost_f = f_items_to_pay_for * cost_f_single

    else:
        total_cost_f = quantity_f * cost_f_single

    return total_cost_f


def simple_price_calculation(product_price: int, quantity: int) -> int:
    total_cost = quantity * product_price

    return total_cost


def single_deal_calculation(product_price: int, product_deal_price: int, deal_quantity: int, quantity: int) -> int:
    if quantity >= deal_quantity:
        if quantity % deal_quantity == 0:
            # have they bought exactly the right amount for the deal
            total_cost = (quantity / deal_quantity) * product_deal_price
        else:
            total_cost = (math.floor(quantity / deal_quantity) * product_deal_price) \
                           + ((quantity % deal_quantity) * product_price)
    elif quantity < 0:
        total_cost = 0
        return total_cost
    else:
        total_cost = quantity * product_price

    return total_cost


def other_item_free_deal_calculation(quantity: int, deal_quantity: int, product_price: int) -> tuple:

    number_of_free_items = math.floor(quantity / deal_quantity)
    total_cost = quantity * product_price

    return total_cost, number_of_free_items


def same_item_free_deal_calculation(quantity: int, deal_quantity: int, product_price: int) -> int:
    if quantity >= deal_quantity:
        quantity_of_free_items = math.floor(quantity / deal_quantity)
        items_to_pay_for = quantity - quantity_of_free_items
        total_cost = items_to_pay_for * product_price

    else:
        total_cost = quantity * product_price

    return total_cost
