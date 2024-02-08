"""
Быстрая сортировка

Логика. Выбираем опорный элемент и расставляем слева элементы, которые меньше опорного,
        а справа, которые больше. Вызываем рекурсию для этих подмассивов пока
        не придем к базовому случаю (len(arr) <= 1). Это способ разделяй и властвую
Сложность n*logn
"""


def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]  # опорный элемент

        less = [x for x in arr[1:] if x < pivot]
        large = [x for x in arr[1:] if x >= pivot]

        return quick_sort(less) + [pivot] + quick_sort(large)


def main():
    arr = [10, 8, 20, 4, -1, 40, -10]

    print(quick_sort(arr))  # [-10, -1, 4, 8, 10, 20, 40]


if __name__ == '__main__':
    main()
