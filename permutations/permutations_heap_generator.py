def permutations(a, size):
    if size == 1:
        yield a
        pass
    else:
        for i in range(size):
            yield from permutations(a, size-1)
            if size & 1:
                a[0], a[size-1] = a[size-1], a[0]
            else:
                a[i], a[size-1] = a[size-1], a[i]


if __name__ == '__main__':
    a = 0
    for x in permutations([1, 2, 3], 3):
        if a % 2 != 0:
            print(x)
        a += 1
