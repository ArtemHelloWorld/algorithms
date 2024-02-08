N = int(input())
string = input()

minn = float('inf')
maxx = float('-inf')

l = 0
r = 0
while r < N:
    if string[r] == '#':
        length = r - l
        if length > maxx:
            maxx = length
        if length < minn:
            minn = length
        l = r + 1
    r += 1
if l != r:
    length = r - l
    if length > maxx:
        maxx = length
    if length < minn:
        minn = length

print(minn, maxx)



