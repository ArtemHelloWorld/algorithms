def is_prime(n):
    for i in range(2, n // 2 + 1):
        if n % i == 0:
            return False
    return True

def solution(n):
    return sum([i if is_prime(i) else 0 for i in range(2, n)])


assert 2  == solution(3)
assert 4227  == solution(200)
assert 76127  == solution(1000)