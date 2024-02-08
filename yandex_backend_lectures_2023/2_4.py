def calculate():
    counter = {}
    for number in numbers:
        counter.setdefault(number, 0)
        counter[number] += 1

    minn = float('inf')

    for k, v in counter.items():
        if k + 1 in counter:
            minn = min(minn, n - v - counter[k + 1])
    if minn == float('inf'):
        return n - max(counter.values())
    return minn


n = int(input())
numbers = [int(x) for x in input().split()]

answer = calculate()
print(answer)
