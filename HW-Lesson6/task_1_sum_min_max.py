# В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.
# вызывать из командной строки:
# python task_1_sum_min_max --min=[мин. элемент массива] --max=[макс. элемент массива] --size=[размер массива]
# пример: python task_1_sum_min_max.py --min=-10 --max=10 --size=50


from helpers.memory_profiler import profiler
from random import randint
import getopt
import sys


# @profiler(verbose=True)
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


@profiler(verbose=True)
def main(arr_min, arr_max, arr_size):
    arr_min, arr_max, arr_size = int(arr_min), int(arr_max), int(arr_size)
    array = [randint(arr_min, arr_max) for _ in range(arr_size)]
    result = largest_negative(array, arr_min)

    print(f'Исходный массив: {array}')
    if result['key'] is not None:
        print(f'Макисмальное отрицательное цисло: {result["value"]} в позиции {result["key"]}')
    else:
        print('Отрицательных чисел в массиве нет')


if __name__ == '__main__':
    try:
        opts, args = getopt.getopt(sys.argv[1:], '', ['max=', 'size=', 'min='])
        main(opts[0][1], opts[1][1], opts[2][1])
    except getopt.GetoptError:
        print('Неверные параметры!')
        sys.exit(1)
    except ValueError:
        print('Неверные параметры!')
        sys.exit(1)


#  Python 3.6.5, x64
#  Результаты:
#  python task_1_sum_min_max.py --min=-10 --max=10 --size=50

#  Переменная - arr_size, тип <class 'int'>: 14
#  Переменная - arr_min, тип <class 'int'>: 14
#  Переменная - arr_max, тип <class 'int'>: 14
#  Переменная - result, тип <class 'dict'>: 136
#          Переменная - value-ключ, тип <class 'str'>: 30
#          Переменная - value-значение, тип <class 'int'>: 14
#          Переменная - key-ключ, тип <class 'str'>: 28
#          Переменная - key-значение, тип <class 'int'>: 14
#  Переменная - array, тип <class 'list'>: 268
#          Переменная - 1-й элемент, тип <class 'int'>: 14
#          Переменная - 2-й элемент, тип <class 'int'>: 14
#          Переменная - 3-й элемент, тип <class 'int'>: 14
#          Переменная - 4-й элемент, тип <class 'int'>: 14
#          Переменная - 5-й элемент, тип <class 'int'>: 14
#          Переменная - 6-й элемент, тип <class 'int'>: 14
#          Переменная - 7-й элемент, тип <class 'int'>: 14
#          Переменная - 8-й элемент, тип <class 'int'>: 12
#          Переменная - 9-й элемент, тип <class 'int'>: 12
#          Переменная - 10-й элемент, тип <class 'int'>: 14
#          Переменная - 11-й элемент, тип <class 'int'>: 14
#          Переменная - 12-й элемент, тип <class 'int'>: 14
#          Переменная - 13-й элемент, тип <class 'int'>: 12
#          Переменная - 14-й элемент, тип <class 'int'>: 14
#          Переменная - 15-й элемент, тип <class 'int'>: 14
#          Переменная - 16-й элемент, тип <class 'int'>: 14
#          Переменная - 17-й элемент, тип <class 'int'>: 14
#          Переменная - 18-й элемент, тип <class 'int'>: 14
#          Переменная - 19-й элемент, тип <class 'int'>: 14
#          Переменная - 20-й элемент, тип <class 'int'>: 14
#          Переменная - 21-й элемент, тип <class 'int'>: 14
#          Переменная - 22-й элемент, тип <class 'int'>: 14
#          Переменная - 23-й элемент, тип <class 'int'>: 14
#          Переменная - 24-й элемент, тип <class 'int'>: 14
#          Переменная - 25-й элемент, тип <class 'int'>: 14
#          Переменная - 26-й элемент, тип <class 'int'>: 14
#          Переменная - 27-й элемент, тип <class 'int'>: 14
#          Переменная - 28-й элемент, тип <class 'int'>: 14
#          Переменная - 29-й элемент, тип <class 'int'>: 14
#          Переменная - 30-й элемент, тип <class 'int'>: 14
#          Переменная - 31-й элемент, тип <class 'int'>: 14
#          Переменная - 32-й элемент, тип <class 'int'>: 14
#          Переменная - 33-й элемент, тип <class 'int'>: 12
#          Переменная - 34-й элемент, тип <class 'int'>: 14
#          Переменная - 35-й элемент, тип <class 'int'>: 14
#          Переменная - 36-й элемент, тип <class 'int'>: 14
#          Переменная - 37-й элемент, тип <class 'int'>: 14
#          Переменная - 38-й элемент, тип <class 'int'>: 14
#          Переменная - 39-й элемент, тип <class 'int'>: 14
#          Переменная - 40-й элемент, тип <class 'int'>: 14
#          Переменная - 41-й элемент, тип <class 'int'>: 14
#          Переменная - 42-й элемент, тип <class 'int'>: 12
#          Переменная - 43-й элемент, тип <class 'int'>: 14
#          Переменная - 44-й элемент, тип <class 'int'>: 14
#          Переменная - 45-й элемент, тип <class 'int'>: 14
#          Переменная - 46-й элемент, тип <class 'int'>: 14
#          Переменная - 47-й элемент, тип <class 'int'>: 14
#          Переменная - 48-й элемент, тип <class 'int'>: 14
#          Переменная - 49-й элемент, тип <class 'int'>: 14
#          Переменная - 50-й элемент, тип <class 'int'>: 14
# ----------------------------------------
# Всего памяти выделено: 1164 bytes
