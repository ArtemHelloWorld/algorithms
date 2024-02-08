n = int(input())
heights = list(map(int, input().split()))

for i in range(1, len(heights)-1):
    if heights[i-1] < heights[i] > heights[i+1]:
        print(i+1)
        break

