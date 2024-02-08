N, M = tuple(map(int, input().split()))

pd = []
for i in range(N):
    row = list(map(int, input().split()))
    way = [-1]*M

    if i == 0:
        for j in range(1, M):
            row[j] += row[j-1]
            way[j] = 'R'
    else:
        row[0] += pd[i-1][0][0]
        way[0] = 'D'
        for j in range(1, M):
            if row[j-1] > pd[i-1][j][0]:
                row[j] += row[j-1]
                way[j] = 'R'
            else:
                row[j] += pd[i-1][j][0]
                way[j] = 'D'
    pd.append(list(zip(row, way)))
print(pd[-1][-1][0])

y, x = N-1, M-1
way = []
while pd[y][x][1] != -1:
    way.append(pd[y][x][1])

    if pd[y][x][1] == 'R':
        x -= 1
    else:
        y -= 1

for x in way[::-1]:
    print(x, end=' ')

