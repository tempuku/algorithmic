import collections
import itertools
import sys


def prime_factors(n):
    i = 2
    while i * i <= n:
        if n % i == 0:
            n /= i
            yield i
        else:
            i += 1

    if n > 1:
        yield n


def prod(iterable):
    result = 1
    for i in iterable:
        result *= i
    return result


def get_divisors(n):
    pf = prime_factors(n)
    pf_with_multiplicity = collections.Counter(pf)
    powers = [
        [factor ** i for i in range(count + 1)]
        for factor, count in pf_with_multiplicity.items()
    ]
    for prime_power_combo in itertools.product(*powers):
        yield prod(prime_power_combo)


def find_divisor(n, k):
    divisors = get_divisors(n)
    try:
        for i in range(k-1):
            divisors.__next__()
        result = divisors.__next__()
    except StopIteration:
        return -1
    else:
        return result


if __name__ == '__main__':
    stdin = sys.stdin
    params = [int(x) for x in stdin.readline().split()]
    # print(find_divisor(*params))
    print(list(prime_factors(params[0])))