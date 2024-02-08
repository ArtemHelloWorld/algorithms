from collections import deque


def read_from_console():
    n, k = map(int, input().split())
    desks = sorted(list(map(int, input().split())))
    return n, k, desks


def main():
    n, k, desks = read_from_console()
    queue = deque(desks[:n-k])
    ans = queue[-1] - queue[0]

    for i in range(n-k, n):
        queue.popleft()
        queue.append(desks[i])
        ans = min(queue[-1] - queue[0], ans)
    return ans


print(main())
