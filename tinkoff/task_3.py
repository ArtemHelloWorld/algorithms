def calculate(n: int, a: list, b: list):
    left = 0
    right = n - 1

    while left != n and a[left] == b[left]:
        left += 1
    if left == n:
        return 'YES'
    while right != -1 and a[right] == b[right]:
        right -= 1
    if left == right:
        return 'NO'
    return 'YES' if sorted(a[left:right+1]) == b[left:right+1] else 'NO'
def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    print(calculate(n, a, b))


if __name__ == '__main__':
    main()


