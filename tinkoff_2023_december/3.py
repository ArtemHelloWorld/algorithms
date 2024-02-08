n, m = tuple(map(int, input().split()))
presents = list(map(int, input().split()))

# случай когда мы не сможем купить ни одного подарка
minn_present = min(presents)
maxx_ost = minn_present - 1

for i in range(minn_present + 1, m + 1):
    for present in presents:
        if present < i:
            i -= present
        elif present == i:
            break
    else:
        maxx_ost = max(i, maxx_ost)
print(maxx_ost)
"""
8 30
10 3 4 6 10 12 4 8
2 12
5 1
8 10
8 1 2 4 8 10 2 4
"""