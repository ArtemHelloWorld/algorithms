N = int(input())
k = int(input())
petya_ryad = int(input())
petya_mesto = int(input())
petya_mesto_linear = (petya_ryad - 1) * 2 + petya_mesto


def answer():
    verh_mesto_linear = petya_mesto_linear + k
    verh_mesto = 2 - (verh_mesto_linear % 2)
    verh_ryad = ((verh_mesto_linear - verh_mesto) // 2) + 1

    niz_mesto_linear = petya_mesto_linear - k
    niz_mesto = 2 - (niz_mesto_linear % 2)
    niz_ryad = ((niz_mesto_linear - niz_mesto) // 2) + 1

    if verh_mesto_linear <= N and niz_mesto_linear > 0:
        if verh_ryad - petya_ryad <= petya_ryad - niz_ryad:
            return f'{verh_ryad} {verh_mesto}'
        else:
            return f'{niz_ryad} {niz_mesto}'
    elif verh_mesto_linear <= N:
        return f'{verh_ryad} {verh_mesto}'
    elif niz_mesto_linear > 0:
        return f'{niz_ryad} {niz_mesto}'

    return '-1'


print(answer())
