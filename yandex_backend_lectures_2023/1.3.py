def read_data():
    with open('input.txt', 'r') as file:
        n = int(file.readline())
        prices = [int(x) for x in file.readline().split()]
    return n, prices


def write_data(answer):
    with open('output.txt', 'w') as file:
        file.write(answer)


def calculate(n, prices):
    if n < 2:
        return 0, 0

    if n == 2:
        if prices[0] < prices[1]:
            return 0, 1
        return 0, 0

    min_price_in_past = 0
    max_price_index = 0
    min_price_index = 0

    for i in range(1, n):
        if prices[i] * prices[min_price_index] > prices[max_price_index] * prices[min_price_in_past]:
            max_price_index = i
            min_price_index = min_price_in_past

        if prices[i] < prices[min_price_in_past]:
            min_price_in_past = i

    if max_price_index != 0 and min_price_index != 0:
        return min_price_index + 1, max_price_index + 1

    return 0, 0


def main():
    n, prices = read_data()

    start, end = calculate(n, prices)
    print(f'{start} {end}')
    write_data(f'{start} {end}')


if __name__ == '__main__':
    main()
