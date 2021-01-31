def permutations(a, size):
    if size == 1:
        print(a)
        pass
    else:
        for i in range(size):
            permutations(a, size-1)
            a[size-1], a[i] = a[i], a[size-1]


if __name__ == '__main__':
    permutations([1, 2, 3, 4, 5, 6, 7, 8], 8)
