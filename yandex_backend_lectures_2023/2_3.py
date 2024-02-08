def short_word(word):
    for i in range(len(word)):
        word_slice = word[:i]
        if word_slice in dictionary:
            return word_slice
    return word


def calculate() -> str:
    return ' '.join(short_word(word) for word in message)


dictionary = set(input().split())
message = input().split()

answer = calculate()
print(answer)
