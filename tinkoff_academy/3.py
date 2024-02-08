n, m, q = tuple(map(int, input().split()))

labyrinth = []

for _ in range(n):
    labyrinth.append(list(map(int, input().split())))

for _ in range(q):
    x, y, k = tuple(map(int, input().split()))
    axy = labyrinth[x-1][y-1]

    count = -2

    # по строке x
    for i in labyrinth[x-1]:
        if abs(axy - i) <= k:
            count += 1
    # по столбцу y
    for string in labyrinth:
        if abs(axy - string[y-1]) <= k:
            count += 1
    print(count)
