from collections import deque

n = int(input())
queue = deque()

for i in range(n):
    action_str = input()
    action = action_str[0]

    if action == '1':
        queue.append(action_str[2])
    elif action == '2':
        for _ in range(len(queue)):
            el = queue.popleft()
            queue.extend([el, el])
    elif action == '3':
        print(queue.popleft())




