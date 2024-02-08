n = int(input())
stickers_have = sorted(int(x) for x in set(input().split()))
len_stickers_have = len(stickers_have)


def find(collectioner):
    l = - 1
    r = len_stickers_have -1

    while l < r:
        m = (l + r + 1) // 2
        if stickers_have[m] < collectioner:
            l = m
        else:
            r = m - 1
    return l


k = int(input())
for collectioner in input().split():
    print(find(int(collectioner)) + 1)
