from random import randint


def bubble_sort(array):
    for i in range(len(array) - 1):
        for j in range(len(array) - 1 - i):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
    return array


unsortedArray = [randint(-100, 100) for _ in range (10)]
print(f'Массив до сортировки: {unsortedArray}')
print(f'Массив после сортировки: {bubble_sort(unsortedArray)}')
