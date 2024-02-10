"""
Написать функцию, которая принимает массив чисел и число,
а возвращает количество подмассивов,
сумма которых равна заданному числу.
"""
from collections import defaultdict


def func(arr: list, n: int) -> int:
    """Префикс со словарем | O(N) | O(N)"""
    ans = 0
    summ = 0
    prefix = defaultdict(int)
    prefix[0] = 1

    for x in arr:
        summ += x
        ans += prefix[summ - n]
        prefix[summ] += 1
    return ans


assert func([], 0) == 0
assert func([2], 1) == 0
assert func([1, 1, 1, 1], 1) == 4
assert func([-2, 4, 2], 4) == 2
assert func([2, 2, 2], 4) == 2

