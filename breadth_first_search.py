"""
Поиск в ширину (Breadth first search, BFS)

Логика: Используем очередь, проверяем первый элемент и добавляем в конец очереди всех соседей
        Сохраняем в словарь visited вершину, которую мы проверили и вершину из которой к ней пришли...
        это позволит восстановить путь с помощью restore_path, если такой существует
"""

import collections


def breadth_first_search(start, end, graph):
    queue = collections.deque([start])  # очередь поиска
    visited = {start: None}

    while queue:
        current_node = queue.popleft()

        if current_node == end:
            break

        next_nodes = graph[current_node]
        for next_node in next_nodes:
            if next_node not in visited:
                queue.append(next_node)
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
        0: [1, 2],
        1: [2],
        2: [3],
        3: [1, 2]
    }

    paths = breadth_first_search(0, 3, graph)
    print(restore_path(0, 3, paths))  # [0, 2, 3]


if __name__ == '__main__':
    main()
