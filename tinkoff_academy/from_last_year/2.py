from collections import deque


def difference(arr1: deque, arr2: list, length: int) -> int:
    return length - sum(arr1[i] == arr2[i] for i in range(length))


s = list(input())
t = list(input())

len_t = len(t)
slise = deque(s[:len_t])
s = s[len_t:]
minn = difference(slise, t, len_t)

for x in s:
    slise.popleft()
    slise.append(x)
    minn = min(difference(slise, t, len_t), minn)

print(minn)
