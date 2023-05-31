import math
from typing import Union

# noinspection PyUnusedLocal
# skus = unicode string


def checkout(skus: str) -> int:
    supermarket_item_dict = parse_string(skus)

    # invalid string return -1
    if supermarket_item_dict == -1:
        return -1

    # calculate the cost of A items
    total_cost_a = calcualte_cost_of_a_item(supermarket_item_dict)
    # calculate the cost of B items
    total_cost_b = calculate_cost_of_b_item(supermarket_item_dict)
    # Calculate cost of C items
    total_cost_c = calculate_cost_c_item(supermarket_item_dict)
    # Calculate cost of D items
    total_cost_d = calculate_cost_d_item(supermarket_item_dict)

    total_cost = total_cost_a + total_cost_b + total_cost_c + total_cost_d

    return total_cost


def parse_string(skus: str) -> Union[int, dict]:
    """ Store number of each item in a dictionary"""
    supermarket_item_dict = {
        "A": 0,
        "B": 0,
        "C": 0,
        "D": 0
    }
    # loop through the string to determine how many of each item is required and return -1 if an invalid input is given
    for char in skus:
        if char != "A" and char != "B" and char != "C" and char != "D":
            return -1
        else:
            supermarket_item_dict[char] += 1

    return supermarket_item_dict


def calcualte_cost_of_a_item(supermarket_item_dict: dict) -> int:
    quantity_a = supermarket_item_dict["A"]
    cost_a_single = 50
    bulk_price_a = 130
    old_bulk_quantity_a = 3
    new_bulk_quantity_a = 5

    # check if there is more than 2 a items bought to calculate deal price
    if 2 < quantity_a < new_bulk_quantity_a:
        if quantity_a % old_bulk_quantity_a == 0:
            # they have bought a multiple 3 amount of item A
            total_cost_a = (quantity_a / old_bulk_quantity_a) * bulk_price_a

        else:
            total_cost_a = (math.floor(quantity_a / old_bulk_quantity_a) * bulk_price_a) \
                           + ((quantity_a % old_bulk_quantity_a) * cost_a_single)
    # check if they have bought a multiple of 5
    elif quantity_a >= new_bulk_quantity_a:
        
    else:
        total_cost_a = quantity_a * cost_a_single

    return total_cost_a


def calculate_cost_of_b_item(supermarket_item_dict: dict) -> int:
    quantity_b = supermarket_item_dict["B"]
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
    else:
        total_cost_b = quantity_b * cost_b_single

    return total_cost_b


def calculate_cost_c_item(supermarket_item_dict: dict) -> int:
    quantity_c = supermarket_item_dict["C"]
    cost_c_single = 20

    total_cost_c = quantity_c * cost_c_single

    return total_cost_c


def calculate_cost_d_item(supermarket_item_dict: dict) -> int:
    quantity_d = supermarket_item_dict["D"]
    cost_d_single = 15
    total_cost_d = quantity_d * cost_d_single

    return total_cost_d


