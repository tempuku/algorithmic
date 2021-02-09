def permutations(a, size):
    if size == 1:
        print(a)
        pass
    else:
        for i in range(size):
            permutations(a, size-1)
            if size & 1:
                a[0], a[size-1] = a[size-1], a[0]
            else:
                a[i], a[size-1] = a[size-1], a[i]


if __name__ == '__main__':
    permutations([1, 2, 3], 3)
