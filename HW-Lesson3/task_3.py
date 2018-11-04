# В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.

from random import randint

ARR_MAX = 100
ARR_SIZE = 10

array = [randint(0, ARR_MAX) for _ in range(ARR_SIZE)]

min_num = ARR_MAX
max_num = 0
min_index = 0
max_index = 0

i = 0
for num in array:
    if num > max_num:
        max_num = num
        max_index = i
    if num < min_num:
        min_num = num
        min_index = i
    i += 1

print(f'Исходный массив: {array}')

array[min_index] = max_num
array[max_index] = min_num

print(f'Минимальное число - {min_num} с индексом {min_index}')
print(f'Максиимальное число - {max_num} с индексом {max_index}')

print(f'Результат: {array}')
