n, m = map(int, input().split())
points = []

for _ in range(n):
    a, b = map(int, input().split())
    a, b = min(a, b), max(a, b)
    points.append((a, 0))
    points.append((b, 2))

m_points = list(map(int, input().split()))
for m_point in m_points:
    points.append((m_point, 1))

points.sort()

ans = {}
count = 0
for point in points:
    if point[1] == 0:
        count += 1
    elif point[1] == 1:
        ans[point[0]] = count
    elif point[1] == 2:
        count -= 1

for a in m_points:
    print(ans[a], end=' ')





