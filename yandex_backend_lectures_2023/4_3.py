l, n, m = tuple(map(int, input().split()))

counter = {}

for _ in range(n):
    start, end = tuple(map(int, input().split()))
    counter.setdefault(start, 0)
    counter.setdefault(end+1, 0)

    counter[start] += 1
    counter[end+1] -= 1

table = []

summ = 0
for i in range(1, l+1):
    summ += counter.get(i, 0)
    table.append(summ)


for _ in range(m):
    print(table[int(input()) - 1])
