class Town:
    def __init__(self, index, price, search_town=-1):
        self.index = index
        self.price = price
        self.search_town = search_town


N = int(input())
towns = [Town(i, x) for i, x in enumerate(input().split())]


stack = []

for town in towns:
    while stack and stack[-1].price > town.price:
        migration = stack.pop()
        migration.search_town = town.index
    stack.append(town)

for town in sorted(towns, key=lambda x: x.index):
    print(town.search_town, end=' ')
