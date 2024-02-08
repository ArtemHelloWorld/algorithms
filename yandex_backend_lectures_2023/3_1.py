n = int(input())
numbers = list(map(int, input().split()))

counter = 0
positive_count = [counter]

for number in numbers:
    if number > 0:
        counter += 1
    positive_count.append(counter)

q = int(input())
for _ in range(q):
    start, end = tuple(map(int, input().split()))
    print(positive_count[end] - positive_count[start - 1])

