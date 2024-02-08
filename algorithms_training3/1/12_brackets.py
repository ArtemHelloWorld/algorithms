opened = '([{'
closed = ')]}'

stack = []

string = input()
for char in string:
    if char in opened:
        stack.append(char)
    else:
        if not len(stack) or opened.index(stack.pop()) != closed.index(char):
            print('no')
            break
else:
    print('yes' if not len(stack) else 'no')


