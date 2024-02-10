def func(string: str) -> tuple[int, int]:
    """Два указателя | Время О(N) | Память O(K)"""
    len_set = len(set(string))

    minn = float('inf')
    minn_l, minn_r = 0, 0

    counter = dict()
    unique = 0
    l = 0
    r = 0
    while r < len(string):
        letter_r = string[r]
        if letter_r not in counter:
            unique += 1
            counter[letter_r] = 0
        counter[letter_r] += 1

        while counter[string[l]] > 1:
            counter[string[l]] -= 1
            l += 1

        if unique == len_set and r - l + 1 < minn:
            minn = r - l + 1
            minn_l, minn_r = l, r
        r += 1

    return minn_l, minn_r



assert func('') == (0, 0)
assert func('a') == (0, 0)
assert func('aaaa') == (0, 0)
assert func('abcd') == (0, 3)
assert func('aaccbabbccaa') == (3, 5)
assert func('aaaabc') == (3, 5)
assert func('abcaaa') == (0, 2)




