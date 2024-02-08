def check(ohrana):
    if ohrana[0][0] != 0:
        return 'Wrong Answer'

    pokritie = 0
    for i, ohr in enumerate(ohrana):
        if ohr[0] > pokritie:
            return 'Wrong Answer'
        if ohr[1] <= pokritie:
            return 'Wrong Answer'
        if i >= 2 and ohr[0] <= ohrana[i-2][1]:
            return 'Wrong Answer'
        pokritie = ohr[1]
    return 'Accepted' if pokritie == 10000 else 'Wrong Answer'


K = int(input())

for _ in range(K):
    string = list(map(int, input().split()))
    N = string[0]
    ohrana = []
    for i in range(1, N*2+1, 2):
        start, finish = string[i], string[i+1]
        if start >= finish:
            raise ZeroDivisionError(start, finish)
        ohrana.append((start, finish))
    # print(ohrana)
    ohrana.sort()

    print(check(ohrana))



"""
2
3 0 3000 2500 7000 2700 10000
2 0 3000 2700 10000

1
5 0 1 1 2 2 3 3 4 4 10000


"""