import math
from typing import Union

# noinspection PyUnusedLocal
# skus = unicode string


supermarket_item_dict = {
        "E": [0, 40, "free deal 1", [2, "B"]],
        "N": [0, 40, "free deal 1", [3, "M"]],
        "R": [0, 50, "free deal 1", [3, "Q"]],
        "A": [0, 50, "complex deal", [3, 130], [5, 200]],
        "B": [0, 30, "simple deal", [2, 45]],
        "C": [0, 20, "single"],
        "D": [0, 15, "single"],
        "F": [0, 10, "free deal 2", 3],
        "G": [0, 20, "single"],
        "H": [0, 10, "complex deal", [5, 45], [10, 80]],
        "I": [0, 35, "single"],
        "J": [0, 60, "single"],
        "K": [0, 80, "simple deal", [2, 150]],
        "L": [0, 90, "single"],
        "M": [0, 15, "single"],
        "O": [0, 10, "single"],
        "P": [0, 50, "simple deal", [5, 200]],
        "Q": [0, 30, "simple deal", [3, 80]],
        "S": [0, 20, "group deal"],
        "T": [0, 20, "group deal"],
        "U": [0, 40, "free deal 2", 4],
        "V": [0, 50, "complex deal", [2, 90], [3, 130]],
        "W": [0, 20, "single"],
        "X": [0, 17, "group deal"],
        "Y": [0, 20, "group deal"],
        "Z": [0, 21, "group deal"]
    }


def checkout(skus: str) -> int:
    supermarket_item_dict = parse_string(skus)

    # invalid string return -1
    if supermarket_item_dict == -1:
        return -1

    easy_ones_total = 0
    simple_deal_total = 0
    free_deal_1_total = 0
    free_deal_2_total = 0
    complex_deal_total = 0

    group_deal_dict = {
        "Z": 0,
        "S": 0,
        "Y": 0,
        "T": 0,
        "X": 0
    }
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

        elif supermarket_item_dict[product_name][2] == "complex deal":
            data = supermarket_item_dict.get(product_name)
            product_price = data[1]
            quantity = data[0]

            small_deal_quantity = data[3][0]
            small_deal_price = data[3][1]

            large_deal_quantity = data[4][0]
            large_deal_price = data[4][1]

            complex_deal_total += complex_deal_calculation(product_price, small_deal_price, large_deal_price,
                                                           small_deal_quantity, large_deal_quantity, quantity)

        elif supermarket_item_dict[product_name][2] == "group deal":
            data = supermarket_item_dict.get(product_name)
            group_deal_dict[product_name] = data[0]

    group_deal_total = group_deal_quantity_calculation(group_deal_dict)
    total_cost = complex_deal_total + simple_deal_total + easy_ones_total + free_deal_1_total + free_deal_2_total \
                 + group_deal_total

    return total_cost


def parse_string(skus: str) -> Union[int, dict]:
    """ Store number of each item in a dictionary"""

    # loop through the string to determine how many of each item is required and return -1 if an invalid input is given
    for char in skus:
        quantity = supermarket_item_dict.get(char, None)
        if quantity is None:
            return -1
        else:
            supermarket_item_dict[char][0] += 1

    return supermarket_item_dict


def simple_price_calculation(product_price: int, quantity: int) -> int:
    if quantity < 0:
        total_cost = 0
    else:
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

    elif quantity < 0:
        total_cost = 0
        return total_cost
    else:
        total_cost = quantity * product_price

    return total_cost


def complex_deal_calculation(product_price: int, small_product_deal_price: int, large_product_deal_price: int,
                             small_deal_quantity: int, large_deal_quantity: int, quantity: int):
    if small_deal_quantity - 1 < quantity < large_deal_quantity:
        if quantity % small_deal_quantity == 0:
            # they have bought something to be used with the small deal
            total_cost = (quantity / small_deal_quantity) * small_product_deal_price
        else:
            total_cost = (math.floor(quantity / small_deal_quantity) * small_product_deal_price) \
                         + ((quantity % small_deal_quantity) * product_price)

    elif quantity >= large_deal_quantity:
        # Check if they have bought a multiple of 5
        if quantity % large_deal_quantity == 0:
            total_cost = (quantity / large_deal_quantity) * large_product_deal_price
        else:
            # check if remainder is equal or larger than the small price deal
            remainder = quantity % large_deal_quantity
            if remainder >= small_deal_quantity:
                single_purchases = remainder - small_deal_quantity
                total_cost = (math.floor(quantity / large_deal_quantity) * large_product_deal_price) \
                             + small_product_deal_price + (single_purchases * product_price)
            else:
                total_cost = (math.floor(quantity / large_deal_quantity) * large_product_deal_price) \
                             + (remainder * product_price)
    elif quantity < 0:
        total_cost = 0
        return total_cost
    else:

        total_cost = quantity * product_price

    return total_cost


def group_deal_quantity_calculation(group_deal_dict: dict) -> int:
    deal_quantity = 3
    deal_cost = 45
    total_quantity = sum(group_deal_dict.values())

    if total_quantity % deal_quantity == 0:
        # exact number of products for the deal
        total_cost = (total_quantity / deal_quantity) * deal_cost

    else:
        # there are items remaining which need to paid at normal price
        # prioritise the most expensive item
        remainder = total_quantity % deal_quantity
        for product in group_deal_dict:
            while total_quantity >= deal_quantity:
            # loop through the dict removing the items until total_quantity is 0
            
                if group_deal_dict[product] <= total_quantity:
                    total_quantity -= group_deal_dict[product]
                    group_deal_dict[product] = 0
                else:
                    group_deal_dict[product] -= total_quantity
                    total_quantity - group_deal_dict[product]

        total_cost = (math.floor(total_quantity / deal_quantity) * deal_cost) + group_deal_remainder_cost_calculation(
            group_deal_dict)

    return total_cost


def group_deal_remainder_cost_calculation(group_deal_dict: dict) -> int:

    s_total = group_deal_dict.get("S") * supermarket_item_dict.get("S")[1]
    t_total = group_deal_dict.get("T") * supermarket_item_dict.get("T")[1]
    x_total = group_deal_dict.get("X") * supermarket_item_dict.get("X")[1]
    y_total = group_deal_dict.get("Y") * supermarket_item_dict.get("Y")[1]
    z_total = group_deal_dict.get("Z") * supermarket_item_dict.get("Z")[1]

    total_cost = sum([s_total, t_total, x_total, y_total, z_total])

    return total_cost





