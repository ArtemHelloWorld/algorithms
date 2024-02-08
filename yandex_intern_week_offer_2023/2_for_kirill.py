n, k = map(int, input().split())
desks = sorted(list(map(int, input().split())))

minn = desks[-1] - desks[0]

left = 0
right = n - k - 1

while right != n:
    minn = min(minn, desks[right] - desks[left])
    left += 1
    right += 1

print(minn)
