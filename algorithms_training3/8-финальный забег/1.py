N = int(input())

stack = []

for c in range(N):
    command = input().strip()
    if 'add' in command:
        command = command.replace('add', '', 1).strip()
        for x in command.split(' ', 1):
            if x.isnumeric():
                for i in range(int(x)):
                    stack.append(command.replace(x, '', 1).strip())

    elif 'delete' in command:
        for i in range(int(command.replace('delete', '', 1).strip())):
            stack.pop()
    elif 'get' in command:
        print(stack.count(command.replace('get', '', 1).strip()))




