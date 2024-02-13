"""
Написать класс с двумя методами. Первый - принимает очередной запрос вида userId, time.
Второй говорит, сколько за последние 5 минут было пользователей, которые совершили хотя бы
1000 запросов.
"""

# ЕСЛИ ЗАПРОСЫ В ХРОНОЛОГИЧЕСКОМ ПОРЯДКЕ -
# ИДЕМ С КОНЦА ДО ПЕРВОГО НЕ ПОДХОДЯЩЕГО
# ЛУЧШЕ ДАЖЕ БИНПОИСКОМ


import time
from collections import defaultdict


class Server:
    def __init__(self):
        self.data = defaultdict(list)

    def register(self, userId, time_):
        self.data[userId].append(time_)

    def count(self):
        ans = 0
        for val in self.data.values():
            if len(val) < 1000:
                break
            else:
                count = 0
                now = int(time.time())
                for x in val:
                    if now - x <= 5 * 60:
                        count += 1
                ans += int(count >= 1000)
        return ans

