# Отсортировать по убыванию методом «пузырька» одномерный целочисленный массив, заданный случайными числами на
# промежутке [-100; 100). Вывести на экран исходный и отсортированный массивы.
import random


def cocktail_sort(array):
    for i in range(len(array) // 2):
        swap = False
        for j in range(1 + i, len(array) - i):
            if array[j] > array[j - 1]:
                array[j], array[j - 1] = array[j - 1], array[j]
                swap = True
        if not swap:
            break
        swap = False
        for j in range(len(array) - i - 1, i, -1):
            if array[j] > array[j - 1]:
                array[j], array[j - 1] = array[j - 1], array[j]
                swap = True
        if not swap:
            break


test = [i for i in range(-100, 101)]
random.shuffle(test)

print(test)
cocktail_sort(test)
print(test)
