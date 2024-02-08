N = int(input())

dp = [[0] * N]
for i in range(N):
    x = int(input())

    for coupon_count, row in enumerate(dp):
        if coupon_count == len(dp) - 1:
            row[i] = row[i - 1] + x
        else:
            row[i] = min(dp[coupon_count + 1][i - 1], row[i - 1] + x)

    if x > 100:
        dp.append([0] * N)
        for k in range(len(dp) - 1, 0, -1):
            dp[k][i] = dp[k - 1][i]
        dp[0][i] = float('inf')

minn = float('inf')
minn_i = -1
k1 = -1
for i, x in enumerate(dp):
    if x[-1] <= minn:
        minn = x[-1]
        minn_i = i
        k1 = i
k2 = []
y = minn_i
x = N - 1

while x != 0:
    if dp[0][x] == float('inf'):
        y -= 1
    if y != len(dp) - 1 and dp[y][x] == dp[y + 1][x - 1]:
        y += 1
        k2.append(x)
    x -= 1
print(minn)
print(k1, len(k2))
for k in k2[::-1]:
    print(k+1)
