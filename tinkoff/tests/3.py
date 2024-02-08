import tinkoff.task_3

n = 3
a = [3, 1, 5, 1]
b = [4, 1, 1, 5]
ans = 'YES'
# ans = 'NO'
print(tinkoff.task_3.calculate(n, a, b))
assert tinkoff.task_3.calculate(n, a, b) == ans
