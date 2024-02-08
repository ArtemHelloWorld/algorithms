`N = int(input())
ans = set()

for _ in range(N):
    x, y = tuple(map(int, input().split()))
    ans.add(x)

print(len(ans))

`