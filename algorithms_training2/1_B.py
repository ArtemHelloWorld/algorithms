N, i, j = map(int, input().split())

forward = max(i, j) - min(i, j) - 1
back = min(i, j) + N - max(i, j) - 1
print(min(forward, back))
