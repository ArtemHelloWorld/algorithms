from collections import defaultdict

counter = defaultdict(int)
with open('input.txt', 'r') as file:
    for line in file:
        for char in line:
            if char not in (" ", "\n"):
                counter[char] += 1

max_count = max(counter.values())

counter_items = sorted(counter.items())
with open('output.txt', 'w') as file:
    for i in range(max_count):
        file.write(''.join('#' if count >= max_count - i else ' ' for letter, count in counter_items) + '\n')
    file.write(''.join([letter for letter, _ in counter_items]))


