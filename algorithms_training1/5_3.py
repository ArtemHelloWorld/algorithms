N = int(input())

last_x, last_y = tuple(map(int, input().split()))
left_to_right = [0]
right_to_left = [0]

for _ in range(N - 1):
    x, y = tuple(map(int, input().split()))
    if last_y > y:
        left_to_right.append(left_to_right[-1])
        right_to_left.append(right_to_left[-1] + last_y - y)
    elif last_y < y:
        left_to_right.append(left_to_right[-1] + y - last_y)
        right_to_left.append(right_to_left[-1])
    else:
        left_to_right.append(left_to_right[-1])
        right_to_left.append(right_to_left[-1])
    last_y = y

M = int(input())
for _ in range(M):
    s, f = tuple(map(int, input().split()))
    s-=1
    f-=1
    if s < f:
        print(left_to_right[f] - left_to_right[s])
    else:
        print(right_to_left[s] - right_to_left[f])
