# Austin Youngren
# Assignment 1: Determine if a list is made up of a repeating pattern.
import math


def get_divisors(list_length):
    divisors = []
    max_div = list_length + 1
    for val in range(1, max_div):
        if (list_length % val == 0) and val not in divisors:
            divisors.append(val)
    return divisors


def is_prime(divisors, list_length):
    return (divisors == [1, list_length])


def repeat(list):
    if list is None:
        return None

    list_length = len(list)
    if (list_length < 2):
        return None

    divisors = get_divisors(list_length)
    if (is_prime(divisors, list_length)):
        for i in range(1, list_length):
            if (list[0] != list[i]):
                return None
        return list[0:1]

    divisors.remove(1)
    divisors.remove(list_length)
    divisors.reverse()

    for div in divisors:
        increment = 0
        aim = (list_length // div) - 1
        section1 = list[0: div]
        for block in range(div, list_length, div):
            block_end = block + div
            if (section1 == list[block:block_end]):
                increment += 1
            else:
                break
        if (increment == aim):
            return section1
    return None
