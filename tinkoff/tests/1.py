import random
import tinkoff.task_1

for i in range(10):
    n = random.randint(1, 10)
    s = random.randint(1, 50)

    ans = None
    zero = False
    a = []
    number = random.randint(1, 2)
    if number > s:
        zero = True
        ans = 0
    while len(a) != n:
        a.append(number)
        if len(a) > 1 and a[-2] <= s < a[-1]:
            ans = a[-2]
        number += random.randint(1, 100)
    if not zero and not ans:
        ans = max(a)
    random.shuffle(a)
    print(n, s, ans, a)
    assert tinkoff.task_1.find_maxx(a, s) == ans, (tinkoff.task_1.find_maxx(a, s), ans)
