from collections import defaultdict

word = input()
len_word = len(word)
counter = defaultdict(int)
count = 0

for i in range(0, (len_word+1) // 2):
    count += len_word - i * 2
    counter[word[i]] += count
    if i != (len_word + (i*(-1)-1)):
        counter[word[i*(-1)-1]] += count

for word, count in sorted(counter.items()):
    print(f'{word}: {count}')

