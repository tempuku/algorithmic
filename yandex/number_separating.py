from collections import Counter
from itertools import combinations_with_replacement, permutations
from random import randint


def number_separating_helper(number: str, max_numbers: float, dashes: int):
    dashes -= 1
    if dashes == 0:
        if len(number) == 1:
            return number, 1
        nums_str = number.replace(' ', '')
        num_list = nums_str.split('-')
        for x in num_list:
            if len(x) > 1 and x[0] == '0':
                return number, float('-inf')
        numbers_counter = Counter(num_list)
        for k in numbers_counter:
            if numbers_counter[k] > 1:
                return number, float('-inf')
        return nums_str, len(numbers_counter)
    nums_str = number[:len(number) - dashes] + '-' + number[-dashes:]
    good_comb_1, max_numbers_1 = number_separating_helper(nums_str, max_numbers, dashes)
    nums_str = number[:len(number) - dashes] + ' ' + number[-dashes:]
    good_comb_2, max_numbers_2 = number_separating_helper(nums_str, max_numbers, dashes)
    if max_numbers_1 > max_numbers_2:
        return good_comb_1, max_numbers_1
    else:
        return good_comb_2, max_numbers_2


def number_separating(number: int):
    number = str(number)
    good_comb = number_separating_helper(number, float('-inf'), len(number))
    return good_comb


def random_with_n_digits(n):
    range_start = 10**(n-1)
    range_end = (10**n)-1
    return randint(range_start, range_end)


if __name__ == '__main__':
    print(number_separating(random_with_n_digits(19)))

