N = int(input())
prices = [(float('inf'), float('inf'), float('inf'))] * 2
for _ in range(N):
    prices.append(tuple(map(int, input().split())))

dp = [0] * 2

for i in range(N):
    dp.append(min(dp[-1] + prices[i+1][1],
                  dp[-2] + prices[i][2],
                  prices[i+1][0]))

print(dp)


