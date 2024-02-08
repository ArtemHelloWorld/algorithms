"""
Бинарный поиск

Только для отсортированных массивов
Сложность: logN
"""


def binary_search(arr, item):
    low = 0
    high = len(arr) - 1

    while low <= high:
        middle = (high + low) // 2
        arr_middle = arr[middle]

        if arr_middle == item:
            return middle
        elif arr_middle < item:
            low = middle + 1
        else:
            high = middle - 1

    return None


def main():
    arr = [1, 4, 7, 8, 10, 15, 18, 32]
    print(binary_search(arr, 32))  # 7


if __name__ == '__main__':
    main()
