def reverse(self, x: int) -> int:
    ans = 0
    sign = -1 if x < 0 else 1
    x *= sign
    if x > (2 ** 31) - 1:
        return 0
    while x:
        ans += x % 10
        ans *= 10
        x //= 10
    ans //= 10
    return ans * sign

print(reverse())