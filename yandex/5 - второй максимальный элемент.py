"""
Написать фунцкию, которая находит в массиве второй максимум.
"""
from typing import Optional


def func(arr: list) -> Optional[int]:
    """Две переменные | Время О(N)| Память О(1)"""
    if len(arr) < 2:
        return None
    maxx1 = float('-inf')
    maxx2 = float('-inf')
    for x in arr:
        if maxx1 < x:
            maxx1, maxx2 = x, maxx1
        elif maxx2 < x < maxx1:
            maxx2 = x
    return maxx2 if maxx2 > float('-inf') else None


assert func([1, 1]) is None
assert func([1, 2]) == 1
assert func([2, 1]) == 1
assert func([1, 4, 3]) == 3
assert func([3, 4, 1]) == 3
