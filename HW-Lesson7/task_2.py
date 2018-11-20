# Отсортируйте по возрастанию методом слияния одномерный вещественный массив, заданный случайными числами на
# промежутке [0; 50). Выведите на экран исходный и отсортированный массивы.
import random


# ф-я для слияния 2х массивов
def merge(left, right, array):
    i = 0
    j = 0
    k = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            array[k] = left[i]
            i = i + 1
        else:
            array[k] = right[j]
            j = j + 1

        k = k + 1

    while i < len(left):
        array[k] = left[i]
        i = i + 1
        k = k + 1

    while j < len(right):
        array[k] = right[j]
        j = j + 1
        k = k + 1


def merge_sort(array):
    n = len(array)
    if n < 2:
        return

    mid = n // 2
    left = []
    right = []

    for i in range(mid):
        left.append(array[i])

    for i in range(mid, n):
        right.append(array[i])

    merge_sort(left)
    merge_sort(right)

    merge(left, right, array)


arr = [i for i in range(51)]
random.shuffle(arr)

print(arr)
merge_sort(arr)
print(arr)
