class RandomizedSet:
    def __init__(self):
        self.lst = []
        self.dict_indexies = {}

    def insert(self, val: int) -> bool:
        if val in self.dict_indexies:
            return False
        self.lst.append(val)
        self.dict_indexies[val] = len(self.lst) - 1
        return True

    def remove(self, val: int) -> bool:
        if val not in self.dict_indexies:
            return False
        val_index = self.dict_indexies[val]

        # move last element to val position
        self.lst[val_index] = self.lst[-1]
        self.dict_indexies[self.lst[-1]] = val_index
        self.lst.pop()
        del self.dict_indexies[val]
        return True

    def getRandom(self) -> int:
        return self.lst[random.randint(0, len(self.lst) - 1)]

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()