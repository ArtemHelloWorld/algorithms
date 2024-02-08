n = int(input())

graph = {
    0: 0
}

maxx = 0
maxx_i = 0
for i in range(1, n+1):
    parent = int(input())
    if maxx < graph[parent] + 1:
        maxx = graph[parent] + 1
        maxx_i = i
    graph[i] = graph[parent] + 1

print(maxx_i)