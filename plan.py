import sys


def plan(dinner_prices):
    pass


if __name__ == '__main__':
    stdin_fileno = sys.stdin
    dinner_prices = []
    for line in stdin_fileno:
        dinner_prices.append(int(line))
    result = plan(dinner_prices)
    sys.stdout.write(str(result))
