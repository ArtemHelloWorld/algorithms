d = int(input())
x, y = map(int, input().split())

if (0 <= x <= -y + d) and (0 <= y <= -x + d):
    print(0)

else:
    a = x ** 2 + y ** 2
    b = (x - d) ** 2 + y ** 2
    c = x ** 2 + (y - d) ** 2
    ans = min(a, b, c)
    if ans == a:
        print(1)
    elif ans == b:
        print(2)
    else:
        print(3)
