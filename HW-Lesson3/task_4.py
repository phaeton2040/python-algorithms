# Определить, какое число в массиве встречается чаще всего.

from random import randint

ARR_MAX = 10
ARR_SIZE = 1000

array = [randint(0, ARR_MAX) for _ in range(ARR_SIZE)]
result = {}

count, item = 0, None
for num in array:
    result[num] = result.get(num, 0) + 1
    if result[num] >= count:
        count, item = result[num], num

print(f'Исходный массив: {array}')
print(f'Наиболее часто встречающийся элемент: {item} ({count} раз(а))')
print(result)
