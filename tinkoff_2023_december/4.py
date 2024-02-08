graph = []

n, k = tuple(map(int, input().split()))
companies_need = set()
for _ in range(k):
    companies_need.add(input())


def find_parent_in_graph(parent_i, graph_):
    if graph_[0] == parent_i:
        return graph_
    else:
        if graph_[3]:
            for g in graph_[3]:
                new_parent = find_parent_in_graph(parent_i, g)
                if new_parent:
                    return new_parent
        return None


for i in range(1, n + 1):
    parent, prise, name = input().split()
    parent = int(parent)
    prise = int(prise)
    if parent == 0:
        graph = [i, prise, name, []]
    else:

        parent_item = find_parent_in_graph(parent, graph)
        parent_item[3].append((i, prise, name, []))

# print(graph)


def buy_graph(graph_):
    global minn_price
    price = graph_[1]
    companies = set(graph_[2])
    for g in graph_[3]:
        p, c = buy_graph(g)
        price += p
        companies.update(c)
    if not companies_need - companies:
        minn_price = min(price, minn_price)
    return price, companies


minn_price = float('inf')
buy_graph(graph)
print(minn_price if minn_price != float('inf') else -1)

"""
4 1
B
0 1 B
1 2 A
2 1 A
1 1 A
"""
