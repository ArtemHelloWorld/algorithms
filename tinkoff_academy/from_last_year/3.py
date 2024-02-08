n = int(input())

points = []

for i in range(n):
    points.append([int(x) for x in input().split()] + [i])


sorted_x = sorted(points, key=lambda x: x[0])
sorted_y = sorted(points, key=lambda x: x[1])

checked = []

for i in [0, 1]:
    x_left = sorted_x[i]
    y_left = sorted_y[i]
    for j in [-1, -2]:
        x_right = sorted_x[j]
        y_right = sorted_y[j]

        checked.append([x_right[0] - x_left[0], x_left[2], x_right[2]])
        checked.append([y_right[1] - y_left[1], y_left[2], y_right[2]])

checked.sort(key=lambda x: x[0], reverse=True)

print(checked)

last_c = checked[0]
for c in checked:
    if not((c[1] == last_c[1] and c[2] == last_c[2]) or (c[2] == last_c[1] and c[1] == last_c[2])):
        print(c[0])
        break




