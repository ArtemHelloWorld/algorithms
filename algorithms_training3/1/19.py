heap = []
len_heap = 0

N = int(input())
for _ in range(N):
    command = input()

    if command[0] == '0':
        integer = int(command.split()[1])
        for i in range(len_heap):
            if heap[i] >= integer:
                heap = heap[:i] + [integer] + heap[i:]
                break
        else:
            heap.append(integer)
        len_heap += 1
    elif command[0] == '1':
        print(heap.pop())
        len_heap -= 1
