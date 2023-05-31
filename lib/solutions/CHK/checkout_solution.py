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
        if char != "A" or char != "B" or char != "C" or char != "D":
            return -1
        else:
            supermarket_item_dict[char] += 1

    # calculate the cost of A items

    quantity_a = supermarket_item_dict["A"]
    cost_a_single = 50
    total_cost_a = 0

    # check if there is more than 2 a items bought to calculate deal price
    if quantity_a > 2:
        if quantity_a % 3 == 0:
            # they have bought a multiple 3 amount of item A
            total_cost_a = (quantity_a / 3) * 130

        else:
            





    return 0
