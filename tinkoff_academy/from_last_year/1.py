t = int(input())

for _ in range(t):
    arr = [int(input()) for x in range(3)]
    arr.sort()
    if (arr[0] + arr[-1]) // 2 == arr[1]:
        print('Yes')
    else:
        print('No')
