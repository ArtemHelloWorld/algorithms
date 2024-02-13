"""
Заменить в строке %20 на пробел
"""


def func(s: str) -> str:
    """Два указателя | Время О(N) | Память O(N)"""
    if len(s) < 3:
        return s

    ans = []
    l = 0
    r = l + 2
    while r < len(s):
        if s[l:r+1] == '%20':
            ans.append(' ')
            l += 3
            r += 3
        else:
            ans.append(s[l])
            l += 1
            r += 1

    while l < len(s):
        ans.append(s[l])
        l += 1

    return ''.join(ans)


assert func('%20') == '%20'.replace('%20', ' ')
assert func('%20%20%20') == '%20%20%20'.replace('%20', ' ')
assert func('a%20b%20c%20d') == 'a%20b%20c%20d'.replace('%20', ' ')

