words = set()

with open('input.txt', 'r') as file:
    strings = file.readlines()

for string in strings:
    for word in string.split():
        words.add(word.strip())

with open('output.txt', 'w') as file:
    file.write(str(len(words)))
