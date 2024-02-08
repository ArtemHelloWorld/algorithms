from collections import deque


deque = deque()


while True:
    command = input()
    if 'push' in command:
        value = int(command.split()[1])
        if 'front' in command:
            deque.appendleft(value)
        elif 'back' in command:
            deque.append(value)
        print('ok')
    elif 'pop' in command:
        if len(deque):
            if 'front' in command:
                print(deque.popleft())
            elif 'back' in command:
                print(deque.pop())
        else:
            print('error')
    elif 'front' in command:
        if len(deque):
            print(deque[0])
        else:
            print('error')
    elif 'back' in command:
        if len(deque):
            print(deque[-1])
        else:
            print('error')
    elif 'size' in command:
        print(len(deque))
    elif 'clear' in command:
        deque.clear()
        print('ok')
    elif 'exit' in command:
        print('bye')
        break

