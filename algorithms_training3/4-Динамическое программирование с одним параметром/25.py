import sys

N = int(input())
x = sorted(list(map(int, input().split())))

if N == 2:
    print(x[1]-x[0])
    sys.exit(0)

dp = [0, x[1]-x[0], x[1]-x[0] + x[2]-x[1]]

for i in range(3, N):
    dp.append(min(dp[-1], dp[-2]) + (x[i] - x[i-1]))

print(dp[-1])
