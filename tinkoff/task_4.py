def find_summ(summ: int, lst: list, counter={}):
    if summ == 0:
        return counter

    for i in range(len(lst)-1, -1, -1):
        if lst[i] * 2 <= summ:
            c_copy = counter.copy()
            c_copy[lst[i]] = 2
            ans = find_summ(summ - lst[i] * 2, lst[:i], c_copy)
            if ans != -1:
                return ans
            else:
                counter[lst[i]] = 0
        elif lst[i] <= summ:
            c_copy = counter.copy()
            c_copy[lst[i]] = 1
            ans = find_summ(summ - lst[i], lst[:i], c_copy)
            if ans != -1:
                return ans
            else:
                counter[lst[i]] = 0
    return -1


n, m = list(map(int, input().split()))
a = sorted(list(map(int, input().split())))
summ = find_summ(n, a)
if summ == -1:
    print(summ)
else:
    print(sum(summ.values()))
    for k in summ.keys():
        print(f'{k} ' * summ[k], end='')



