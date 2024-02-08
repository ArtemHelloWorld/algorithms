v = int(input())

tree = [[i, [], 1] for i in range(v)]

for _ in range(v - 1):
    parent, child = sorted(list(map(int, input().split())))
    tree[parent-1][1].append(child-1)

for vertex in tree[::-1]:
    for child in vertex[1]:
        vertex[2] += tree[child][2]

print(' '.join(list(map(lambda x: str(x[2]), tree))))

