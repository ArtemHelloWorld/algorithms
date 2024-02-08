import math

with open('input.txt', 'r') as file:
    n = int(file.readline())

k = math.floor((-1 + math.sqrt(1 + 8 * n)) / 2)

with open('output.txt', 'w') as file:
    file.write(str(k))

