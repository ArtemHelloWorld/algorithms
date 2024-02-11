"""
Создать класс с ассимптотиками unordered map, а также способной равновероятно выдавать
один из входящих элементов
"""

import random


class UnorderedMap:
    def __init__(self):
        self.map = {}

    def __setitem__(self, key, value):
        self.map[key] = value

    def __getitem__(self, key):
        return self.map.get(key)

    def getRandomElement(self):
        keys = list(self.map.keys())
        return self.map[random.choice(keys)]


class UnorderedMapCustom:
    _k = 10
    def __init__(self):
        self.unordered_map = [None] * self._k

    def __setitem__(self, key, value):
        _hash = hash(key) % self._k
        node = self.Node(key, value)

        if self.unordered_map[_hash] is None:
            self.unordered_map[_hash] = node
        else:
            el = self.unordered_map[_hash]
            while el.next is not None:
                el = el.next
            el.next = node

    def __getitem__(self, key):
        _hash = hash(key) % self._k
        if self.unordered_map[_hash] is None:
            return None
        else:
            el = self.unordered_map[_hash]
            while el.key != key or el.next is not None:
                el = el.next
            return None if el.key != key else el.value

    def get_random_element(self):
        key = random.choice(range(self._k))
        i = 1
        while self.unordered_map[key] is None and i < self._k:
            key = (key + i) % self._k
            i += 1
        if not self.unordered_map[key]:
            return None

        el = self.unordered_map[key]
        while el.next is not None:
            if random.randint(0, 100) > 50:
                return el.value
            el = el.next
        return el.value

    class Node:
        def __init__(self, key, value, next=None):
            self.key = key
            self.value = value
            self.next = next


unordered_map = UnorderedMapCustom()
unordered_map[1] = '1'
unordered_map[2] = '2'
unordered_map[3] = '3'
unordered_map[4] = '4'
unordered_map[5] = '5'
unordered_map[6] = '6'
unordered_map[7] = '7'
unordered_map[8] = '8'
assert unordered_map[1] == '1'
assert unordered_map[6] == '6'
assert unordered_map[8] == '8'
print(unordered_map.get_random_element())
