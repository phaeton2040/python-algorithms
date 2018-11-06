# Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран. Например,
# если введено число 3486, то надо вывести число 6843.

import cProfile

def reverse_num_loop(num):
    reversed_num = ''

    while num != 0:
        last_digit = num % 10
        num = num // 10
        reversed_num = f'{reversed_num}{last_digit}'
    return reversed_num

# python -m timeit -n 100 -s "import task_1_recursion" "task_1_recursion.reverse_num_loop(1111111111)"
# 100 loops, best of 3: 3.46 usec per loop

# python -m timeit -n 100 -s "import task_1_recursion" "task_1_recursion.reverse_num_loop(11111111111111111111)"
# 100 loops, best of 3: 7.6 usec per loop

# python -m timeit -n 100 -s "import task_1_recursion" "task_1_recursion.reverse_num_loop(111111111111111111111111111111)"
# 100 loops, best of 3: 12.1 usec per loop

def reverse_num_recursion(num):
    num = str(num)
    if len(num) == 0:
        return num
    else:
        return reverse_num_recursion(num[1:]) + num[0]


# python -m timeit -n 100 -s "import task_1_recursion" "task_1_recursion.reverse_num_recursion(1111111111)"
# 100 loops, best of 3: 5.71 usec per loop

# python -m timeit -n 100 -s "import task_1_recursion" "task_1_recursion.reverse_num_recursion(11111111111111111111)"
# 100 loops, best of 3: 10.9 usec per loop

# python -m timeit -n 100 -s "import task_1_recursion" "task_1_recursion.reverse_num_recursion(111111111111111111111111111111)"
# 100 loops, best of 3: 15.6 usec per loop

# cProfile.run('reverse_num_recursion(1111111111)') 11/1    0.000    0.000    0.000    0.000 task_1_recursion.py:24(reverse_num_recursion)
# cProfile.run('reverse_num_recursion(11111111111111111111)') 21/1    0.000    0.000    0.000    0.000 task_1_recursion.py:24(reverse_num_recursion)
# cProfile.run('reverse_num_recursion(111111111111111111111111111111)') 31/1    0.000    0.000    0.000    0.000 task_1_recursion.py:24(reverse_num_recursion)

# Вывод: оба алгоритма в целом эквивалентны по сложности и быстродействию
# алгоритм, использующий цикл, немного быстрее за счет того, что в нем используются операции с целыми числами, а в рекурсивном - срез строки
