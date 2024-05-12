import random

def get_numbers_ticket(min, max, quantity):
    """ticket number generator"""

    if min < 1 or max > 1000 or quantity < 1 or quantity > (max - min + 1):
        return "Wrong input data, pls check that min>1, max <=1000 and min<=quantity>=max"

    numbers = random.sample(range(min, max + 1), quantity)
    numbers.sort()

    return numbers
