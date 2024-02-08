n, q = tuple(map(int, input().split()))
a = list(map(int, input().split()))

for _ in range(q):
    event = input()
    if event[0] == '+':
        l, r, x = tuple(map(int, event[2:].split()))
        if x != 0:
            for i in range(l, r + 1):
                a[i - 1] += x
    elif event[0] == '?':
        l, r, k, b = tuple(map(int, event[2:].split()))
        maxx = float('-inf')
        for i in range(l, r + 1):
            val = min(a[i - 1], k * i + b)
            if maxx < val:
                maxx = val
        print(maxx)
