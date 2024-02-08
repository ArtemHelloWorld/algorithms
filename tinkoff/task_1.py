def find_maxx(lst: list, money: int):
    maxx = 0
    for i in lst:
        if i == money:
            return money
        elif i < money:
            maxx = max(maxx, i)
    return maxx

n, s = map(int, input().split())
a = list(map(int, input().split()))

print(find_maxx(a, s))




