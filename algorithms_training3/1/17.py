from collections import deque


first = deque(map(int, input().split()))
second = deque(map(int, input().split()))

count = 0
while count < 10 ** 6 and first and second:
    card_first = first.popleft()
    card_second = second.popleft()
    count += 1

    winner = -1
    if card_first == 0 and card_second == 9:
        winner = 1
    elif card_first == 9 and card_second == 0:
        winner = 2
    else:
        winner = 1 if card_first > card_second else 2

    if winner == 1:
        first.append(card_first)
        first.append(card_second)
    elif winner == 2:
        second.append(card_first)
        second.append(card_second)

if not first:
    print(f'second {count}')
elif not second:
    print(f'first {count}')
else:
    print('botva')
