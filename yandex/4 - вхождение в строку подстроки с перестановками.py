"""
Написать функцию, которая находит в строке количество вхождений заданной строки
 с точностью до её перестановки (заданной строки)
 f(”abacb” , ”abc”) = 2
"""


def func(string: str, substring: str) -> int:
    """Два указателя | Время О(N) | Память О(Ksub + Nsub) = О(Nsub)"""
    if len(string) < len(substring):
        return 0

    substring_dict = dict()  # Память О(Ksub)
    for s in substring:
        substring_dict[s] = substring_dict.get(s, 0) + 1

    counter = dict()  # О(Nsub)
    l = 0
    r = 0
    ans = 0

    while r < len(substring):
        counter[string[r]] = counter.get(string[r], 0) + 1
        r += 1

    while r < len(string):
        ans += int(counter == substring_dict)
        counter[string[r]] = counter.get(string[r], 0) + 1
        counter[string[l]] = counter.get(string[l], 0) - 1
        r += 1
        l += 1
    ans += int(counter == substring_dict)
    return ans


assert func('aa', 'ab') == 0
assert func('ab', 'ab') == 1
assert func('aba', 'ab') == 2
assert func('abab', 'ab') == 3
assert func('ababbbbb', 'ab') == 3
assert func('ababbbbb', 'aa') == 0
assert func('ababbbbbc', 'aa') == 0
