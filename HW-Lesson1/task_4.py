# Написать программу, которая генерирует в указанных пользователем границах:
# -- случайное целое число;
# -- случайное вещественное число;
# -- случайный символ.
# Для каждого из трех случаев пользователь задает свои границы диапазона.
# Например, если надо получить случайный символ от 'a' до 'f', то вводятся эти символы.
# Программа должна вывести на экран любой символ алфавита от 'a' до 'f' включительно.

# считаем пользователя идеальным и расчитываем,
# что он введет целые числа или прописные английские буквы в качестве границ диапазона

import random

min_range = input('Min: ')
max_range = input('Max: ')
is_numeric = True

try:
    min_range = int(min_range)
    max_range = int(max_range)

    print('Введены числа')
except ValueError:
    print('Введены символы')
    min_range = ord(min_range)
    max_range = ord(max_range)
    is_numeric = False
finally:
    if min_range > max_range:
        a = max_range
        max_range = min_range
        min_range = a

    if is_numeric:
        print(f'Случайное целое число: {random.randint(min_range, max_range)}')
        print(f'Случайное вещественное число: {random.triangular(min_range, max_range)}')
    else:
        print(f'Случайный символ: {chr(random.randint(min_range, max_range))}')
    print('Конец')
