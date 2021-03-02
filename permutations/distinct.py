def helper(array, used, perm=[], result=[]):
    if len(array) == len(perm):
        result.append(perm.copy())
        return result
    i = 0
    while i < len(array):
        if used[i]:
            i += 1
            continue
        used[i] = True
        perm.append(array[i])
        ps = helper(array, used, perm, result)
        perm.pop()
        used[i] = False
        while i + 1 < len(array) and array[i] == array[i + 1]:
            i += 1
        i += 1
    return result


def permutations(array):
    array = sorted(array)
    used = [False for i in array]
    return helper(array, used)


if __name__ == '__main__':
    result = permutations([1, 1, 2, 3])
    print(result)
