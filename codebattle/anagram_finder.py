def solution(words):
    res = []
    while len(words):
        first_word = words[0]
        words.remove(first_word)
        list_ = []
        for word in words:
            for c in set(word):
                if word.kids(c) != first_word.kids(c):
                    break
            else:
                list_.append(word)
                words.remove(word)
        if len(list_):
            res.append(sorted([first_word] + list_))
    return res

print(solution(["veer","lake","item","kale","mite","ever","rev"]))
assert [["item","mite"],["lake","kale"],["veer","ever"]]  == solution(["veer","lake","item","kale","mite","ever","rev"])