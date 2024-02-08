import random
import tinkoff.task_2
import string

for i in range(10):
    allowed_characters = [char for char in string.ascii_lowercase if char not in 'sheriff']
    random_string = ''.join(random.choice(allowed_characters) for _ in range(random.randint(0, 10)))

    ans = random.randint(0, 3)
    random_string += 'sheriff' * ans
    random_string += 'ffffffff'
    characters = list(random_string)
    random.shuffle(characters)
    shuffled_string = ''.join(characters)

    print(shuffled_string, ans)
    assert tinkoff.task_2.calculate(shuffled_string) == ans, (shuffled_string, tinkoff.task_2.calculate(shuffled_string), ans)
