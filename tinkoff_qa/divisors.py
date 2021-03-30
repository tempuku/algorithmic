import sys
import math


def divisor_generator(n):
    divisors = []
    for i in range(1, int(math.sqrt(n) + 1)):
        if n % i == 0:
            yield i
            if i*i != n:
                divisors.append(n / i)
    for divisor in reversed(divisors):
        yield divisor


def find_divisor(n, k):
    divisors = divisor_generator(n)
    try:
        for i in range(k-1):
            divisors.__next__()
        result = divisors.__next__()
    except StopIteration:
        return -1
    else:
        return int(result)


if __name__ == '__main__':
    stdin = sys.stdin
    params = [int(x) for x in stdin.readline().split()]
    print(find_divisor(*params))
