from collections import defaultdict


t = int(input())
pattern = {
    'T': 1,
    'I': 1,
    'N': 1,
    'K': 1,
    'O': 1,
    'F': 2,
}

for _ in range(t):
    letters = input()
    if len(letters) != 7:
        print('No')
        continue
    count = defaultdict(int)
    for letter in letters:
        if letter not in pattern:
            print('No')
            break
        count[letter] += 1
    else:
        print('Yes' if count == pattern else 'No')


"""
4
TINKAOF
TINKOFFF
AAAA
FFOKNIT
"""