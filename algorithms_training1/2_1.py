def check(lst: list):
    last = float('-inf')
    for n in lst:
        if n <= last:
            return 'NO'
        last = n
    return 'YES'


numbers = list(map(int, input().split()))
print(check(numbers))

