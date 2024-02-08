def good(m, k, stalls):
    count = 1
    prev = stalls[0]
    for i in range(1, len(stalls)):
        if stalls[i] - prev >= m:
            count += 1
            prev = stalls[i]
    return count >= k


n, k = map(int, input().split())
stalls = list(map(int, input().split()))
l = 0
r = stalls[-1] - stalls[0]
while r > l:
    m = (l + r + 1) // 2
    if good(m, k, stalls):
        l = m
    else:
        r = m - 1

print(l)
