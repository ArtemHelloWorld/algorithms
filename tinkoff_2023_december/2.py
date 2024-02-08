t = int(input())

for _ in range(t):
    n = int(input())
    a = sorted(list(map(int, input().split())), reverse=True)
    for i in range(1, n):
        for j in range(0, i):
            if a[j] > 0:
                a[j] -= 1
                a[i] -= 1
                break
        else:
            print('No')
            break
    else:
        print('Yes')
