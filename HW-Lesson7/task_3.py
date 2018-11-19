# Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом. Найти в массиве медиану. Медианой
# называется элемент ряда, делящий его на две равные части: в одной находятся элементы, которые не меньше медианы,
# в другой – не больше ее.

import random
import statistics # использую готовый модуль для проверки


# Насколько я понял, алгоритм поиска медианы в массиве - частный случай поиска минимального n-го числа и похож на
# алгоритм быстрой сортировки Такой алгоритм называют quick select
def quick_select(items, item_index):

    # можно обойтись без внутренней функции, но я ее сюда ввел,
    # чтобы упростить сигнатуру внешней
    def select(lst, min_idx, max_idx, index):

        if max_idx == min_idx:
            return lst[min_idx]

        pivot_index = random.randint(min_idx, max_idx)

        lst[min_idx], lst[pivot_index] = lst[pivot_index], lst[min_idx]

        i = min_idx
        for j in range(min_idx + 1, max_idx + 1):
            if lst[j] < lst[min_idx]:
                i += 1
                lst[i], lst[j] = lst[j], lst[i]

        lst[i], lst[min_idx] = lst[min_idx], lst[i]

        if index == i:
            return lst[i]
        elif index < i:
            return select(lst, min_idx, i - 1, index)
        else:
            return select(lst, i + 1, max_idx, index)

    return select(items, 0, len(items) - 1, item_index)


print('Программа считает медиану случайного массива случайных чисел длины 2m + 1')
m = int(input('Введите m: '))
length = 2 * m + 1

array = [i for i in range(length)]
random.shuffle(array)

print(array)

# проверяем с помощью встроенных модулей
assert quick_select(array, length // 2) == statistics.median(array), 'Косяк =('
print(quick_select(array, length // 2))
