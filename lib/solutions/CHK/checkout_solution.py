import math

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus: str) -> int:

    """- param[0] = a String containing the SKUs of all the products in the basket
     - @return = an Integer representing the total checkout value of the items"""

    # not sure what the input data looks like so need to deploy to find out

    """id = CHK_R1_002, req = checkout(""), resp = 0
        id = CHK_R1_003, req = checkout("A"), resp = 0
        id = CHK_R1_004, req = checkout("B"), resp = 0
        id = CHK_R1_005, req = checkout("C"), resp = 0
        id = CHK_R1_006, req = checkout("D"), resp = 0
        id = CHK_R1_007, req = checkout("a"), resp = 0
        id = CHK_R1_008, req = checkout("-"), resp = 0
        id = CHK_R1_009, req = checkout("ABCa"), resp = 0
        id = CHK_R1_010, req = checkout("AxA"), resp = 0
        id = CHK_R1_011, req = checkout("ABCD"), resp = 0
        id = CHK_R1_012, req = checkout("A"), resp = 0
        id = CHK_R1_013, req = checkout("AA"), resp = 0
        id = CHK_R1_014, req = checkout("AAA"), resp = 0
        id = CHK_R1_015, req = checkout("AAAA"), resp = 0
        id = CHK_R1_016, req = checkout("AAAAA"), resp = 0
        id = CHK_R1_017, req = checkout("AAAAAA"), resp = 0
        id = CHK_R1_018, req = checkout("B"), resp = 0
        id = CHK_R1_019, req = checkout("BB"), resp = 0
        id = CHK_R1_020, req = checkout("BBB"), resp = 0
        id = CHK_R1_021, req = checkout("BBBB"), resp = 0
        id = CHK_R1_022, req = checkout("ABCDABCD"), resp = 0
        id = CHK_R1_023, req = checkout("BABDDCAC"), resp = 0
        id = CHK_R1_024, req = checkout("AAABB"), resp = 0
        id = CHK_R1_001, req = checkout("ABCDCBAABCABBAAA")"""

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

    # calculate the cost of A items

    quantity_a = supermarket_item_dict["A"]
    cost_a_single = 50
    bulk_price_a = 130
    bulk_quantity_a = 3

    # check if there is more than 2 a items bought to calculate deal price
    if quantity_a > 2:
        if quantity_a % bulk_quantity_a == 0:
            # they have bought a multiple 3 amount of item A
            total_cost_a = (quantity_a / bulk_quantity_a) * bulk_price_a

        else:
            total_cost_a = (math.floor(quantity_a / bulk_quantity_a) * bulk_price_a) \
                           + ((quantity_a % bulk_quantity_a) * cost_a_single)
    else:
        total_cost_a = quantity_a * cost_a_single

    # calculate the cost of B items

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


    # Calculate cost of C items

    quantity_c = supermarket_item_dict["C"]
    cost_c_single = 20

    total_cost_c = quantity_c * cost_c_single

    # Calculate cost of D items

    quantity_d = supermarket_item_dict["D"]
    cost_d_single = 15

    total_cost_d = quantity_d * cost_d_single

    total_cost = cost_a_single + cost_b_single + cost_c_single + cost_d_single


    return total_cost


