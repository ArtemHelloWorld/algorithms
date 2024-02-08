N, M = tuple(map(int, input().split()))

pd = []
for i in range(N):
    row = list(map(int, input().split()))
    if i == 0:
        for j in range(1, M):
            row[j] += row[j-1]
    else:
        row[0] += pd[i-1][0]
        for j in range(1, M):
            row[j] += min(row[j-1], pd[i-1][j])
    pd.append(row)
print(pd[-1][-1])
