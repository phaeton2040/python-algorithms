# В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.

from random import randint

ARR_SIZE = 10
ARR_MAX = 10
ARR_MIN = -10


def largest_negative(arr, min_val):
    max_negative_num, max_negative_num_idx, i = min_val, None, 0
    for num in arr:
        if 0 > num > max_negative_num:
            max_negative_num = num
            max_negative_num_idx = i
        i += 1
    return {
        'value': max_negative_num,
        'key': max_negative_num_idx
    }


array = [randint(ARR_MIN, ARR_MAX) for _ in range(ARR_SIZE)]
result = largest_negative(array, ARR_MIN)

print(f'Исходный массив: {array}')
if result['key'] is not None:
    print(f'Макисмальное отрицательное цисло: {result["value"]} в позиции {result["key"]}')
else:
    print('Отрицательных чисел в массиве нет')
