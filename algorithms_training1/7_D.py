N = int(input())

shoppers = []
for i in range(N):
    s, f = map(int, input().split())
    if f - s >= 5:
        shoppers.append((s, 0, i))
        shoppers.append((f, 1, i))

shoppers.sort()

if len(shoppers) == 0:
    print(0, 10, 20)
elif len(shoppers) == 1:
    print(1, shoppers[0][0], shoppers[0][0]+10)
else:
    count = set()
    counter = []
    last = shoppers[0]

    for shopper in shoppers:
        if (last[0] != shopper[0]) and last[1] == 0:
            counter.append((last[0], count.copy()))
        if shopper[1] == 1 and (last[1] == 0 or last[0] != shopper[0]):
            counter.append((shopper[0], count.copy()))

        if shopper[1] == 0:
            count.add(shopper[2])
        elif shopper[1] == 1:
            count.remove(shopper[2])
        last = shopper


    # for count in counter:
        # print(count)

    left = 0
    right = 0

    maxx = set()
    maxx_pos = None

    while right != len(counter) - 1:
        while right != len(counter) - 1 and counter[right][0] - counter[left][0] < 5:
            right += 1
        if counter[right][0] - counter[left][0] < 5:
            break
        visitors = counter[right][1] & counter[left][1]
        if len(visitors) > len(maxx):
            maxx = visitors
            maxx_pos = counter[left][0]
        left += 1
    # print(maxx, maxx_pos)

    if maxx_pos is None:
        maxx_pos = 1

    left = 0
    right = 0

    pre_maxx = set()
    pre_maxx_pos = None

    while right != len(counter) - 1:
        if abs(counter[left][0] - maxx_pos) >= 5:
            while right != len(counter) - 1 and counter[right][0] - counter[left][0] < 5:
                right += 1

            if counter[right][0] - counter[left][0] < 5:
                break

            visitors = counter[right][1] & counter[left][1] - maxx
            if len(visitors) > len(pre_maxx):
                pre_maxx = visitors
                pre_maxx_pos = counter[left][0]
        left += 1
    # print(pre_maxx, pre_maxx_pos)
    if pre_maxx_pos is None:
        pre_maxx_pos = maxx_pos + 10
    if pre_maxx_pos > 2 * 10**9 or maxx_pos > 2 * 10 ** 9:
        raise ZeroDivisionError
    print(len(maxx) + len(pre_maxx), min(maxx_pos, pre_maxx_pos), max(maxx_pos, pre_maxx_pos))


"""

7
7 18
8 16
9 18
7 12
14 18
8 13
14 18

"""