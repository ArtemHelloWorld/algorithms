N = int(input())
tshirts = list(map(int, input().split()))
M = int(input())
jeans = list(map(int, input().split()))

best_tshirt = tshirts[0]
best_jeans = jeans[0]
diff = abs(best_tshirt - best_jeans)

curr_jeans = 0

for tshirt in tshirts:
    while curr_jeans != M - 1 and abs(tshirt - jeans[curr_jeans]) > abs(tshirt - jeans[curr_jeans+1]):
        curr_jeans += 1

    if abs(tshirt - jeans[curr_jeans]) < diff:
        diff = abs(tshirt - jeans[curr_jeans])
        best_tshirt = tshirt
        best_jeans = jeans[curr_jeans]


print(best_tshirt, best_jeans)

