stack = []

while True:
    command = input()

    if 'push' in command:
        stack.append(int(command.split()[1]))
        print('ok')
    elif 'pop' in command:
        if len(stack):
            print(stack.pop())
        else:
            print('error')
    elif 'back' in command:
        if len(stack):
            print(stack[-1])
        else:
            print('error')
    elif 'size' in command:
        print(len(stack))
    elif 'clear' in command:
        stack.clear()
        print('ok')
    elif 'exit' in command:
        print('bye')
        break
