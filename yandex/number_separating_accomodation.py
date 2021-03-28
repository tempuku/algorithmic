from collections import Counter
from itertools import combinations_with_replacement, permutations
from random import randint


def number_separating(number):
    max_numbers = float('-inf')
    number = str(number)
    good_comb = ''
    combs = combinations_with_replacement(' -', len(number) - 1)
    for comb in combs:
        combs_with_perms = set(permutations(comb))
        for comb_with_perm in combs_with_perms:
            try:
                num = ''
                for x in range(len(number) - 1):
                    num += number[x] + comb_with_perm[x]
                num += number[-1]
                nums_str = num.replace(' ', '')
                num_list = nums_str.split('-')
                for x in num_list:
                    if len(x) > 1 and x[0] == '0':
                        raise Exception
                numbers_counter = Counter(num_list)
                for k in numbers_counter:
                    if numbers_counter[k] > 1:
                        raise Exception
                if len(numbers_counter) > max_numbers:
                    max_numbers = len(numbers_counter)
                    good_comb = nums_str
            except Exception:
                pass
    return good_comb
        # numbers_count = Counter(number)
        #


def random_with_N_digits(n):
    range_start = 10**(n-1)
    range_end = (10**n)-1
    return randint(range_start, range_end)


if __name__ == '__main__':
    print(number_separating(random_with_N_digits(5)))

