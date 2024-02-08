N = int(input())
numbers = list(map(int, input().split()))
x = int(input())

diff = float('inf')
ans = None

for n in numbers:
    diff_curr = abs(x-n)
    if diff > diff_curr:
        diff = diff_curr
        ans = n

print(ans)