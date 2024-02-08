N, k = list(map(int, input().split()))

dp = [0] * (k-1) + [1]

for _ in range(N-1):
    dp.append(sum(dp[-k:]))

print(dp[-1])
