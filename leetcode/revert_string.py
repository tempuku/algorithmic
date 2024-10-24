def revert_string(a: str):
    array = list(a)
    for i in range(len(array)//2):
        if array[i] != array[len(array)-i-1]:
            return False
    return True

if __name__ == "__main__":
    a = "123321"
    print(revert_string(a))

    b = "1234321"
    
    print(revert_string(b))

    c = "13242"
    print(revert_string(c))
