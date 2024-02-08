def sum_of_digits(x: int) -> int:
    return sum(int(digit) for digit in str(x))


def compressor(x: int) -> int:
    while x > 9:
        x = sum_of_digits(x)
    return x


def main():
    n = int(input())

    for _ in range(n):
        l, r = tuple(map(int, input().split()))
        multiply = 1

        for multiplier in range(l, r + 1):
            multiply *= multiplier

        print(compressor(multiply))


if __name__ == '__main__':
    main()
