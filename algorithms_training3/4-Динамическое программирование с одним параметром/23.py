N = int(input())

integers = [1]
set_integers = set(integers)
dp = [0]
prev = [-1]

i = 0
while True:
    m2 = integers[i] * 2
    m3 = integers[i] * 3
    p1 = integers[i] + 1

    if m2 <= N and m2 not in set_integers:
        integers.append(m2)
        set_integers.add(m2)
        dp.append(dp[i]+1)
        prev.append(i)
    if m3 <= N and m3 not in set_integers:
        integers.append(m3)
        set_integers.add(m3)
        dp.append(dp[i]+1)
        prev.append(i)
    if p1 <= N and p1 not in set_integers:
        integers.append(p1)
        set_integers.add(p1)
        dp.append(dp[i]+1)
        prev.append(i)

    if N in set_integers:
        break
    i += 1

way = []
i = integers.index(N)
print(dp[i])
while i != -1:
    way.append(integers[i])
    i = prev[i]
for x in way[::-1]:
    print(x, end=' ')
