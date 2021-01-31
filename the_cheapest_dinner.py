import sys


def the_cheapest_dinner(dinner_prices):
    used_codes = []
    exist_code = 0
    lowest_price_code = None
    for i, price in enumerate(dinner_prices):
        if price > 100:
            exist_code += 1
            continue
        else:
            if exist_code:
                used_codes.append(i)
                exist_code -= 1
                lowest_price_code = min(dinner_prices[x] for x in used_codes)
            elif used_codes:
                if price > lowest_price_code:
                    del used_codes[used_codes.index(dinner_prices.index(lowest_price_code))]
                    used_codes.append(i)
    return sum(price for i, price in enumerate(dinner_prices) if i not in used_codes)


if __name__ == '__main__':
    stdin_fileno = sys.stdin
    dinner_prices = []
    for line in stdin_fileno:
        dinner_prices.append(int(line))
    result = the_cheapest_dinner(dinner_prices)
    sys.stdout.write(str(result))
