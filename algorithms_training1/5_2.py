N, K = tuple(map(int, input().split()))
numbers = list((map(int, input().split())))

count = 0

summ = 0
prefix = set()
prefix.add(summ)

for number in numbers:
    summ += number
    count += (summ-K) in prefix
    prefix.add(summ)

print(count)


