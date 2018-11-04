# В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами. Сами
# минимальный и максимальный элементы в сумму не включать.

from random import randint

ARR_SIZE = 15
ARR_MAX = 100
ARR_MIN = 0

array = [randint(ARR_MIN, ARR_MAX) for _ in range(ARR_SIZE)]


def get_min_max_range(arr, max_val):
    min_num = max_val
    max_num = 0
    min_index = 0
    max_index = 0

    cnt = 0
    for num in arr:
        if num > max_num:
            max_num = num
            max_index = cnt
        if num < min_num:
            min_num = num
            min_index = cnt
        cnt += 1

    return sorted([min_index, max_index])


# получаем индексы минимального и максимального элементов
min_max_range = get_min_max_range(array, ARR_MAX)

# считаем сумму
min_max_between_sum = 0
for i in range(min_max_range[0] + 1, min_max_range[1]):
    min_max_between_sum += array[i]

print(f'Исходный массив: {array}')
print(f'Максимальный и минимальный элемент находятся на позицияй {min_max_range[0]} и {min_max_range[1]}')
print(f'Сумма элементов, находящихся между {min_max_range[0]} и {min_max_range[1]} позициями - {min_max_between_sum}')

