n = int(input())

count = 0
answer = []
for h in range(1, n+1):
    height = 2 * h - 1
    count += height ** 2
    answer.append(height ** 3 - count)

print(' '.join(list(map(str, answer))))
