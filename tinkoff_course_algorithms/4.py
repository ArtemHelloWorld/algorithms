import sys

N = int(input())
numbers = sorted(list(map(int, input().split())))
answer = []
if N == 1:
    print(numbers[0])
    sys.exit(0)

l = 0
r = 0

for i in range(1, N):
    if numbers[i] == numbers[r] or numbers[i] - 1 == numbers[r]:
        r = i
    else:
        if numbers[l] == numbers[r]:
            answer.append(str(numbers[l]))
        elif numbers[r] - numbers[l] == 1:
            answer.append(str(numbers[l]))
            answer.append(str(numbers[r]))
        else:
            answer.append(str(numbers[l]))
            answer.append('...')
            answer.append(str(numbers[r]))
        l = i
        r = i

if numbers[l] == numbers[r]:
    answer.append(str(numbers[l]))
elif numbers[r] - numbers[l] == 1:
    answer.append(str(numbers[l]))
    answer.append(str(numbers[r]))
else:
    answer.append(str(numbers[l]))
    answer.append('...')
    answer.append(str(numbers[r]))


print(' '.join(answer))
