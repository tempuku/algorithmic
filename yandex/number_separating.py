from collections import Counter
from itertools import combinations_with_replacement


def number_separating(number):
    max_numbers = int('-inf')
    number = str(number)
    combs = combinations_with_replacement(' -', len(number))
    for comb in combs:
        pass
