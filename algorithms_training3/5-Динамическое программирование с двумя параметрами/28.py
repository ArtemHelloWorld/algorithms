N, M = tuple(map(int, input().split()))

pd = [[0] * M for _ in range(N)]
pd[0][0] = 1
for y in range(N):
    for x in range(M):
        if x - 1 >= 0 and y - 2 >= 0:
            pd[y][x] += pd[y - 2][x - 1]
        if x - 2 >= 0 and y - 1 >= 0:
            pd[y][x] += pd[y - 1][x - 2]
print(pd[-1][-1])
