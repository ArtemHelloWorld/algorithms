score = 0

for _ in range(3):
    x, y = tuple(map(float, input().split()))
    x = int(x * 10 ** 18)
    y = int(y * 10 ** 18)
    rr = x ** 2 + y ** 2

    if rr <= 10 ** 34:
        score += 3
    elif 10 ** 34 < rr <= 64 * 10 ** 34:
        score += 2
    elif 64 * 10 ** 34 < rr <= 10 ** 36:
        score += 1
print(score)
