N = int(input())

blocks = {}

for _ in range(N):
    w, h = tuple(map(int, input().split()))
    if w in blocks:
        blocks[w] = max(blocks[w], h)
    else:
        blocks[w] = h


print(sum(list(blocks.values())))

