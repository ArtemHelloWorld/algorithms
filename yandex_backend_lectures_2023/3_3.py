def calculate(bulbs, middle):
    res = []
    for bulb in bulbs:
        count = bulb // middle
        res.append(count)

    return res


def main():
    n, k = list(map(int, input().split()))

    bulbs = []
    for _ in range(k):
        bulbs.append(int(input()))

    left = 0
    right = 40000

    while left <= right:
        middle = (right + left) // 2

        res = calculate(bulbs, middle)

        if n > sum(res):
            right = middle - 1
        else:
            left = middle + 1

    print(right)
    if right == 0:
        return
    else:
        for i, count in enumerate(calculate(bulbs, right)):
            for _ in range(min(n, count)):
                print(i+1)
            n -= count





if __name__ == '__main__':
    main()
