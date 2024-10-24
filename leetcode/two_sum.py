def two_sum(array: list, k: int):
    s = set()
    r = []
    l = []
    for i in array:
        diff = k - i
        if diff in s and not (diff in r or diff in l):
            r.append(i)
            l.append(diff)
        s.add(i)
    return list(zip(l,r))


def two_sum(array: list, k: int):
    a = sort(array)
    r = []
    for i in array:
        for j in array:
            s = a[i] + a[j]  
            if s == k:
                r.append([a[i], a[j]])
            elif s == k:

if __name__ == "__main__":
    a = [1,2,3,4]

    print(two_sum(a, 5))
    
    a = [1,2,3,4,3,2]

    print(two_sum(a, 5))
