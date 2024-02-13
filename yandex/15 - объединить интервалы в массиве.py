"""
Дан список чисел. Вывести в порядке возрастания все числовые последовательности в нем.
Пример: [1, 3, 7, 11, 8, 2] -> "1-3, 7-8, 11".
"""


def func(arr: list) -> str:
    """Два указателя | Время О(NlogN) | Память O(N)"""
    arr.sort()
    ans = []
    l = r = 0
    while r < len(arr) - 1:
        if arr[r] + 1 == arr[r + 1] or arr[r] == arr[r + 1]:
            r += 1
        else:
            if arr[r] == arr[l]:
                ans.append(str(arr[r]))
            else:
                ans.append(f'{arr[l]}-{arr[r]}')
            r += 1
            l = r

    if arr[r] == arr[l]:
        ans.append(str(arr[r]))
    else:
        ans.append(f'{arr[l]}-{arr[r]}')

    return ', '.join(ans)

assert func([1, 3, 7, 11, 8, 2]) == "1-3, 7-8, 11"
assert func([1, 3, 7, 11, 8, 2, 12]) == "1-3, 7-8, 11-12"
