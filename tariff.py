import sys


def tariff(a, b, c, d):
    return a if d < b else a + (d - b) * c


if __name__ == '__main__':
    stdin_fileno = sys.stdin
    input = []
    for line in stdin_fileno:
        input = [int(x) for x in line.split()]
    if input:
        result = tariff(*input)
        sys.stdout.write(str(result))
