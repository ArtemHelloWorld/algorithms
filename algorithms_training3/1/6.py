M = int(input())
N = int(input())

if N == 0:
    print(0)
else:
    os_list = [(i, tuple(map(int, input().split()))) for i in range(N)]
    os_list.sort(key=lambda x: (x[1][0], x[1][1]))

    res = set()
    curr_os = os_list[0]
    for os_i in range(1, N):
        if curr_os[1][1] < os_list[os_i][1][0]:
            res.add(curr_os[0])
            curr_os = os_list[os_i]
        else:
            if curr_os[0] < os_list[os_i][0]:
                if curr_os[0] in res:
                    res.remove(curr_os[0])
                curr_os = os_list[os_i]
            else:
                res.add(curr_os[0])
    res.add(curr_os[0])
    print(len(res))

