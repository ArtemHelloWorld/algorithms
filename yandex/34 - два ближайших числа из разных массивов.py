def func(arr1: list, arr2: list):
    """Два указателя | Время О(N) | Память O(1)"""
    i1 = 0
    i2 = 0
    minn = float('inf')
    while i1 < len(arr1) and i2 < len(arr2):
        minn = min(minn, abs(arr1[i1] - arr2[i2]))

        if arr1[i1] < arr2[i2]:
            i1 += 1
        elif arr2[i2] < arr1[i1]:
            i2 += 1
        else:
            return 0

    return minn


assert func([1, 5, 6], [3, 7, 15]) == 1
assert func([1, 3], [10, 15]) == 7
assert func([10, 15], [1, 3]) == 7
assert func([1, 10, 20], [4, 6, 16]) == 3

