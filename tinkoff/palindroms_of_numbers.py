def generate_palindromes_with_length(l):
    ''' generate a list of palindrome numbers with len(str(palindrome)) == l '''
    if l < 1:
        return []
    if l == 1:
        return [x for x in range(10)]
    p = []
    if (l % 2):
        half_length = (l - 1) / 2
        for x in range(0, 10):
            for y in range(int(10 ** (half_length - 1)), int(10 ** half_length)):
                p.append(int(str(y) + str(x) + str(y)[::-1]))
    else:
        half_length = l / 2
        for x in range(int(10 ** (half_length - 1)), int(10 ** half_length)):
            p.append(int(str(x) + str(x)[::-1]))
    p.sort()
    return p


def generate_palindrome(minx, maxx):
    ''' return a list of palindrome numbers in a given range '''
    min_len = len(str(minx))
    max_len = len(str(maxx))
    p = []
    for l in range(min_len, max_len + 1):
        for x in generate_palindromes_with_length(l):
            if x <= maxx and x >= minx:
                p.append(x)
    p.sort()
    return p


if __name__ == '__main__':
    print(generate_palindrome(0, 144))
