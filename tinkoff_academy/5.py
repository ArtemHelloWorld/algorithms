import copy
n = int(input())

count_a = 0
count_b = 0
count_c = 0

counter = []

for _ in range(n):
    string = input()

    a = string.count('a')
    b = string.count('b')
    c = string.count('c')

    count_a += a
    count_b += b
    count_c += c

    counter.append((a, b, c))


minn_differ = max(count_a, count_b, count_c) - min(count_a, count_b, count_c)
maxx_count = count_a + count_b + count_c

local_bests = [
    (
        count_a,
        count_b,
        count_c,
        max(count_a, count_b, count_c) - min(count_a, count_b, count_c)
    ),
]
for new_a, new_b, new_c in counter:
    new_local_bests = copy.deepcopy(local_bests)
    for i, local_best in enumerate(local_bests):
        new_local_best_a = local_best[0] - new_a
        new_local_best_b = local_best[1] - new_b
        new_local_best_c = local_best[2] - new_c
        new_local_best_diff = max(new_local_best_a, new_local_best_b, new_local_best_c) - min(new_local_best_a, new_local_best_b, new_local_best_c)

        new_local = (new_local_best_a, new_local_best_b, new_local_best_c, new_local_best_diff)

        if i == len(local_bests) - 1:
            new_local_bests.append(new_local)
        else:
            if new_local_best_diff < local_bests[i+1][3] or (new_local_best_diff == local_bests[i+1][3] and sum(new_local[:-1]) > sum(local_bests[i+1][:-1])):
                new_local_bests[i+1] = new_local

        if new_local_best_diff < minn_differ and sum(new_local[:-1]) != 0:
            minn_differ = new_local_best_diff
            maxx_count = sum(new_local[:-1])
        elif new_local_best_diff == minn_differ:
            maxx_count = max(maxx_count, sum(new_local[:-1]))

    local_bests = new_local_bests

print(maxx_count)
