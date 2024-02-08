from collections import deque

queue = deque()


while True:
    command = input()
    if 'push' in command:
        queue.append(int(command.split()[1]))
        print('ok')
    elif 'pop' in command:
        if len(queue):
            print(queue.popleft())
        else:
            print('error')
    elif 'front' in command:
        if len(queue):
            print(queue[0])
        else:
            print('error')
    elif 'size' in command:
        print(len(queue))
    elif 'clear' in command:
        queue.clear()
        print('ok')
    elif 'exit' in command:
        print('bye')
        break

