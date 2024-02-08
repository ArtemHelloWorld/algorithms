N, M, K = tuple(map(int, input().split()))
matrix = []
for i in range(N):
    new_string = list(map(int, input().split()))
    for j in range(1, M):
        new_string[j] += new_string[j-1]
    if i != 0:
        for j in range(M):
            new_string[j] += matrix[-1][j]
    matrix.append(new_string)


# for i in range(N):
#     for j in range(M):
#         print(matrix[i][j], end=' ')
#     print()

for _ in range(K):
    x1, y1, x2, y2 = tuple(map(int, input().split()))
    x1, y1, x2, y2 = x1 - 1, y1 - 1, x2 - 1, y2 - 1

    ans = matrix[x2][y2]

    if y1 != 0:
        ans -= matrix[x2][y1-1]
    if x1 != 0:
        ans -= matrix[x1-1][y2]
    if x1 != 0 and y1 != 0:
        ans += matrix[x1-1][y1-1]
    print(ans)
