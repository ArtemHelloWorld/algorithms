def round_up(diff):
    if diff % 4 > 0:
        diff += 4 - (diff % 4)
    return diff

n = int(input())
m = int(input())
c2 = int(input())
c5 = int(input())

diff = m - n

if diff <= 0:
    # покупать ничего не нужно
    price = 0
elif c5 <= c2:
    # Делать +1 не выгодно. Берём всё по +4
    diff = round_up(diff)
    price = diff // 4 * c5
elif c5 <= c2 * 2:
    # Делать +1+1 невыгодно. Но выгодно +1.
    # Берем всё по +4, а если останется 1, то делаем +1
    price = 0
    if diff % 4 == 1:
        price += c2
        diff -= diff % 4
    diff = round_up(diff)
    price += diff // 4 * c5
elif c5 <= c2 * 3:
    # Делать +1+1+1 невыгодно. Но выгодно +1 или +1+1.
    # Берем всё по +4, а если останется 1 или 2, то делаем +1
    price = 0
    if diff % 4 in (1, 2):
        price += c2 * (diff % 4)
        diff -= diff % 4
    diff = round_up(diff)
    price += diff // 4 * c5

elif c5 <= c2 * 4:
    # Делать +1+1+1+1 невыгодно. Но выгодно +1 или +1+1 или +1+1+1.
    # Берем всё по +4, а если останется 1 или 2 или 3, то делаем +1
    price = 0
    if diff % 4 in (1, 2, 3):
        price += c2 * (diff % 4)
        diff -= diff % 4
    diff = round_up(diff)
    price += diff // 4 * c5
else:
    # Делать +4 невыгодно. Берём всё по +1
    price = diff * c2
print(price)
