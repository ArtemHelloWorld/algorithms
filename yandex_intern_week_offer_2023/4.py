import sys
from collections import defaultdict


def main():
    k, n, m = map(int, input().split())

    roads = defaultdict(list)
    for _ in range(n):
        day, road = map(int, input().split())
        roads[road].append(day)

    sad_days_count = 0
    intervals = []
    for days in roads.values():
        sad_days_count += days[-1] - days[0]
        for i in range(len(days) - 1):
            intervals.append(days[i + 1] - days[i])
        m -= 1
        if m == -1:
            print(m)
            sys.exit()

    intervals.sort()
    for _ in range(min(m, len(intervals))):
        sad_days_count -= intervals.pop()

    return sad_days_count


print(main())

"""
5 7 6
1 2 
2 3
2 1
6 2
7 4
9 4
13 4 
---> 2

5 7 5
1 2 
2 3
2 1
6 2
7 4
9 4
13 4 
--> 6
"""
