"""
Написать функцию, которая делает RLE сжатие строки,
 например "abbccc"→ "ab2c3"
"""


def func(string: str) -> str:
    """Два указателя с ограничивающим символом | Время О(N) | Память О(N) """
    string += '$'

    ans = []
    l = 0
    r = 0

    while r < len(string) - 1:
        if string[r + 1] == string[l]:
            r += 1
        else:
            if r == l:
                ans.append(f'{string[l]}')
            else:
                ans.append(f'{string[l]}{r - l + 1}')
            r += 1
            l = r
    return ''.join(ans)


assert func('') == ''
assert func('a') == 'a'
assert func('aa') == 'a2'
assert func('aaa') == 'a3'
assert func('ab') == 'ab'
assert func('aabb') == 'a2b2'
assert func('abbccc') == 'ab2c3'


def func(string: str) -> str:
    """Два указателя | Время О(N) | Память О(N) """
    if len(string) <= 1:
        return string
    ans = []
    l = 0
    r = 1

    while r < len(string):
        if string[r] != string[l]:
            if r - l == 1:
                ans.append(f'{string[l]}')
            else:
                ans.append(f'{string[l]}{r - l}')
            l = r
        r += 1
    if l == len(string) - 1:
        ans.append(f'{string[l]}')
    else:
        ans.append(f'{string[l]}{len(string) - l}')
    return ''.join(ans)


assert func('') == ''
assert func('a') == 'a'
assert func('aa') == 'a2'
assert func('aaa') == 'a3'
assert func('ab') == 'ab'
assert func('aabb') == 'a2b2'
assert func('abbccc') == 'ab2c3'
