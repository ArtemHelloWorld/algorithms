k = int(input())
string = input()
len_string = len(string)

res = 0

for char in set(string):
    left_index = 0
    right_index = 0
    k_local = k - (not string[left_index] == char)

    while right_index != len_string - 1:
        right_index += 1
        if string[right_index] != char:
            k_local -= 1

        while k_local < 0 and right_index > left_index:
            if string[left_index] != char:
                k_local += 1
            left_index += 1

        res = max(right_index - left_index + 1, res)
    if k_local >= 0:
        res = max(right_index - left_index + 1, res)


print(res)

"""
1
aaabbb
неправильно считает
"""
