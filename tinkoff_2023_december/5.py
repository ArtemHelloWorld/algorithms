n, m, q = tuple(map(int, input().split()))

kids_values = tuple(map(int, input().split()))
kids = {}
for i in range(n):
    kids[i+1] = [kids_values[i], []]

for _ in range(m):
    u, v = tuple(map(int, input().split()))
    kids[u][1].append(v)
    kids[v][1].append(u)

for _ in range(q):
    event = input()
    if event[0] == '+':
        kid, count = tuple(map(int, event[1:].strip().split()))
        for friend in kids[kid][1]:
            kids[friend][0] += count
    elif event[0] == '?':
        print(kids[int(event.split()[1])][0])
