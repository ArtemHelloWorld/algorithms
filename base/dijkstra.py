"""
Алгоритм Дейкстры для самого дешевого пути во взвешенном графе

"""


def dijkstra(start, end, graph):
    queue = [(0, start)]
    cost_visited = {start: 0}
    visited = {start: None}

    while queue:
        current_cost, current_node = queue.pop(0)

        if current_node == end:
            break

        next_nodes = graph[current_node]
        for next_cost, next_node in next_nodes:
            new_cost = cost_visited[current_node] + next_cost

            if next_node not in cost_visited or new_cost < cost_visited[next_node]:
                queue.append((new_cost, next_node))
                cost_visited[next_node] = new_cost
                visited[next_node] = current_node

    return visited


def restore_path(start, end, paths):
    if end not in paths:
        return None

    current_node = end
    path = [end]

    while current_node != start:
        current_node = paths[current_node]
        path.append(current_node)

    return path[::-1]


def main():
    graph = {
        'A': [(2, 'M'), (3, 'P')],
        'M': [(2, 'A'), (2, 'N')],
        'N': [(2, 'M'), (2, 'B')],
        'P': [(3, 'A'), (4, 'B')],
        'B': [(4, 'P'), (2, 'N')],
    }

    start = 'A'
    end = 'B'

    path = dijkstra(start, end, graph)

    print(restore_path(start, end, path))  # ['A', 'M', 'N', 'B']


if __name__ == '__main__':
    main()
