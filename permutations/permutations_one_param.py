def permutations(array):
    if len(array) == 1:
        return [array]
    else:
        perms = []
        for i in range(len(array)):
            rest = array[:i] + array[i+1:]
            # print(f'{rest=}')
            ps = permutations(rest)
            # print(f'{ps=}')
            current = [array[i]]
            for p in ps:
                perms.append([*current, *p])
        return perms


if __name__ == '__main__':
    result = permutations([1, 2, 3, 4, 5, 6, 7, 8])
    print(result)
