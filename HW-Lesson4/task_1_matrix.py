import cProfile

from random import randint


def get_matrix(rows, cols, arr_max):
    result = []

    row = 0
    while row < rows:
        result.append([])
        col = 0
        while col < cols:
            num = randint(-arr_max, arr_max)
            result[row].append(num)
            col += 1
        row_sum = 0
        for i in result[row]:
            row_sum += i
        result[row].append(row_sum)
        row += 1
    return result


# python -m timeit -n 100 -s "import task_1" "task_1_matrix.get_matrix(10, 10, 100)"
# 100 loops, best of 3: 181 usec per loop

# python -m timeit -n 100 -s "import task_1" "task_1_matrix.get_matrix(20, 20, 100)"
# 100 loops, best of 3: 716 usec per loop

# python -m timeit -n 100 -s "import task_1" "task_1_matrix.get_matrix(30, 30, 100)"
# 100 loops, best of 3: 1.6 msec per loop

# python -m timeit -n 100 -s "import task_1" "task_1_matrix.get_matrix(500, 500, 100)"
# 100 loops, best of 3: 439 msec per loop

# cProfile.run('get_matrix(10, 10, 100)')  1    0.000    0.000    0.000    0.001 task_1_matrix.py:6(get_matrix)
# cProfile.run('get_matrix(20, 20, 100)')  1    0.000    0.000    0.001    0.001 task_1_matrix.py:6(get_matrix)
# cProfile.run('get_matrix(30, 30, 100)')  1    0.001    0.001    0.003    0.003 task_1_matrix.py:6(get_matrix)

def get_matrix_optimized(rows, cols, arr_max):
    result = []

    row = 0
    while row < rows:
        result.append([])
        col = 0
        row_sum = 0
        while col < cols:
            num = randint(-arr_max, arr_max)
            result[row].append(num)
            col += 1
            row_sum += num

        result[row].append(row_sum)
        row += 1
    return result

# python -m timeit -n 100 -s "import task_1" "task_1_matrix.get_matrix_optimized(10, 10, 100)"
# 100 loops, best of 3: 179 usec per loop

# python -m timeit -n 100 -s "import task_1" "task_1_matrix.get_matrix_optimized(20, 20, 100)"
# 100 loops, best of 3: 710 usec per loop

# python -m timeit -n 100 -s "import task_1" "task_1_matrix.get_matrix_optimized(30, 30, 100)"
# 100 loops, best of 3: 1.58 msec per loop

# python -m timeit -n 100 -s "import task_1" "task_1_matrix.get_matrix_optimized(500, 500, 100)"
# 100 loops, best of 3: 449 msec per loop

# cProfile.run('get_matrix_optimized(10, 10, 100)')  1    0.000    0.000    0.000    0.001 task_1_matrix.py:6(get_matrix)
# cProfile.run('get_matrix_optimized(20, 20, 100)')  1    0.000    0.000    0.001    0.001 task_1_matrix.py:6(get_matrix)
# cProfile.run('get_matrix_optimized(30, 30, 100)')  1    0.001    0.001    0.003    0.003 task_1_matrix.py:6(get_matrix)

# Вывод:
# алгоритм создания матрицы случайных чисел произвольного размера достаточно оптимизирован
# удаление из алгоритма доп. цикла для подсчета суммы не играет особой роли.
# Сложность - О(rows * columns).
