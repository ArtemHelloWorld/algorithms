n = int(input())

friends = sorted(
    enumerate([list(map(int, input().split())) for i in range(n)]),
    key=lambda x: (x[1][0], -x[1][1])
)

max_day = 0
res = []
for i, friend in friends:
    if max_day <= friend[0]:
        max_day = friend[1]
    elif friend[0] < max_day < friend[1]:
        friend[0] = max_day
        max_day = friend[1]
    elif friend[1] <= max_day:
        friend = [-1, -1]
    res.append((i, friend))
for _, friend in sorted(res, key=lambda x: x[0]):
    print(f'{friend[0]} {friend[1]}')
