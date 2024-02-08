n = int(input())
heights = list(map(int, input().split()))

count = 0

maxx_height = 0
maxx_i = None
for i, height in enumerate(heights):
    if height > maxx_height:
        maxx_height = height
        maxx_i = i


for mountais in (heights[:maxx_i], heights[maxx_i+1:][::-1]):
    local_maxx = 0
    for height in mountais:
        if height > local_maxx:
            local_maxx = height
        else:
            count += local_maxx - height
print(count)
