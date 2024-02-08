def main():
    n = int(input())

    parents_count = {
        0: 0
    }
    for i in range(1, n + 1):
        parent = int(input())
        parents_count[i] = parents_count.get(parent, 0) + 1

    ans = 0
    maxx_parents = 0
    for k, v in parents_count.items():
        if v > maxx_parents:
            maxx_parents = v
            ans = k
    return ans


print(main())
