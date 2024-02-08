string = input()

left = 0
right = len(string) - 1

while left < right and string[left] == string[right]:
    while string[left] == string[left + 1]:
        left += 1
    left += 1

    while string[right] == string[right-1]:
        right -= 1
    right -= 1

print(max(0, right-left+1))

