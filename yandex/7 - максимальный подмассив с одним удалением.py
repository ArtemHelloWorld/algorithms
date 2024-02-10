"""
Напишите функцию, которая принимает массив 0 и 1,
а возвращает длину максимального подмассива
из единиц после удаления ровно одной цифры.
"""
from collections import defaultdict


def func(arr: list) -> int:
    """Два указателя | O(N) | O(1)"""
    counter = defaultdict(int)
    maxx = 0

    l = 0
    r = 0
    while r < len(arr):
        counter[arr[r]] += 1
        while counter[0] > 1:
            counter[arr[l]] -= 1
            l += 1
        count_1 = counter[1] if counter[0] == 1 else counter[1] - 1
        maxx = max(maxx, count_1)
        r += 1
    return maxx


assert func([]) == 0
assert func([0, 0, 0]) == 0
assert func([0, 0, 1]) == 1
assert func([1, 1, 0]) == 2
assert func([1, 1, 1]) == 2
