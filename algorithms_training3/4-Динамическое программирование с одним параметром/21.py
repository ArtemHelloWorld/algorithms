N = int(input())
dp = [2, 4, 7]
for i in range(3, N):
    dp.append(dp[i-1] + dp[i-2] + dp[i-3])
print(dp[N-1])

