from collections import defaultdict

n, m, k = tuple(map(int, input().split()))

points = defaultdict(dict)
for _ in range(m):
    u, d, v = list(map(int, input().split()))
    points[u][d] = v
    points[v][d] = u

ways = list(map(int, input().split()))

package = 1
for way in ways:
    if way not in points[package]:
        print(0)
        break
    else:
        package = points[package][way]
else:
    print(package)


