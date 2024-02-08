import random

import tinkoff.task_4

for _ in range(100):
    n = random.randint(5, 15)
    m = random.randint(1, 5)
    a = []
    while len(a) != m:
        a_i = random.randint(1, 15)
        if a_i not in a:
            a.append(a_i)
    res = tinkoff.task_4.find_summ(n, a)
    summ = 0
    if res!=-1:
        for k, v in res.items():
            summ += k * v
        print(summ, a, 'aaaaaa')
        assert n == summ, (n, a, res)
    else:
        print(n, a, res)