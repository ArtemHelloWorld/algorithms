k = int(input())

left_x = float('inf')
bottom_y = float('inf')
right_x = float('-inf')
top_y = float('-inf')

for _ in range(k):
   x, y = tuple(map(int, input().split()))
   left_x = min(x, left_x)
   bottom_y = min(y, bottom_y)
   right_x = max(x, right_x)
   top_y = max(y, top_y)

print(f'{left_x} {bottom_y} {right_x} {top_y}')

