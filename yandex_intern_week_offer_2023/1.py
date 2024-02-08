import math


def read_from_console():
    n = int(input())
    m = int(input())
    c2 = int(input())
    c5 = int(input())
    return n, m, c2, c5


def main():
    n, m, c2, c5 = read_from_console()
    diff = m - n

    if diff <= 0:
        return 0

    for rate in (1, 2, 3, 4):
        if c2 * rate >= c5:
            ans = 0
            if diff % 4 < rate:
                ans += (diff % 4) * c2
                diff -= diff % 4
            return ans + math.ceil(diff / 4) * c5
    return diff * c2


print(main())
