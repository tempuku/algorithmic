def permutations(array, perm=[], result=[]):
    if len(array) == 0:
        result.append(perm.copy())
    for i in range(len(array)):
        perm.append(array[i])
        rest = array[:i] + array[i+1:]
        ps = permutations(rest, perm, result)
        perm.pop()
    return result


if __name__ == '__main__':
    result = permutations([1, 2, 3])
    print(result)
