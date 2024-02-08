def answer(letters_list: list):
    len_letters_list = len(letters_list)
    if len_letters_list == 0 or len_letters_list == 1:
        return 0
    elif len_letters_list == 2:
        return min(letters_list) * (len_letters_list - 1)

    min_letters_list = min(letters_list)
    letters_list = [x - min_letters_list for x in letters_list]
    l = 0
    r = 0
    res = min_letters_list * (len_letters_list - 1)
    while r <= len_letters_list - 1:
        if letters_list[r] == 0:
            res += answer(letters_list[l:r])
            l = r + 1
        r += 1
    res += answer(letters_list[l:])
    return res


N = int(input())
letters = [int(input()) for _ in range(N)]

print(answer(letters))
