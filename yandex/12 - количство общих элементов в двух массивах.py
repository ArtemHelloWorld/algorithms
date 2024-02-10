"""
Написать функцию, которая принимает два массива размера N, а возвращает массив размера
N такой, что в k-ой ячейке записано максимальное количество пар, что a[i] = b[j], i, j <= k где a -
первый массив, b - второй. При том каждый элемент не более чем в одной паре.
"""
from collections import defaultdict


def func(a: list, b: list) -> list:
    """Префикс со словарем | O(N) | O(N)"""
    count_a = defaultdict(int)
    count_b = defaultdict(int)

    count = 0
    ans = [0] * len(a)
    for i in range(len(a)):
        count_a[a[i]] += 1
        count_b[b[i]] += 1

        if count_a[a[i]] > 0 and count_b[a[i]] > 0:
            count_a[a[i]] -= 1
            count_b[a[i]] -= 1
            count += 1
        if count_a[b[i]] > 0 and count_b[b[i]] > 0:
            count_a[b[i]] -= 1
            count_b[b[i]] -= 1
            count += 1
        ans[i] = count
    return ans


assert func([], []) == []
assert func([1], [2]) == [0]
assert func([1], [1]) == [1]
assert func([1, 1], [1, 1]) == [1, 2]
assert func([1, 2], [2, 1]) == [0, 2]
assert func([1, 1], [2, 1]) == [0, 1]


