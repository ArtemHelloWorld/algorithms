stack = []

string = input()

for char in string:
    if char.isspace():
        pass
    elif char.isdigit():
        stack.append(int(char))
    elif char == '+':
        stack.append(stack.pop() + stack.pop())
    elif char == '-':
        stack.append(-1 * stack.pop() + stack.pop())
    elif char == '*':
        stack.append(stack.pop() * stack.pop())
print(stack[0])




