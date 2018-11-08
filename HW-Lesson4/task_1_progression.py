# Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...Количество элементов (n) вводится с клавиатуры.


def calculate_n_sum(b1, q, n):
    n_member = b1 * (q ** (n - 1))
    return (1 - n_member * q) / (1 - q)

# python -m timeit -n 100 -s "import task_1_progression" "task_1_progression.calculate_n_sum(1, -0.5, 100)"
# 100 loops, best of 3: 0.563 usec per loop

# python -m timeit -n 100 -s "import task_1_progression" "task_1_progression.calculate_n_sum(1, -0.5, 200)"
# 100 loops, best of 3: 0.555 usec per loop

# python -m timeit -n 100 -s "import task_1_progression" "task_1_progression.calculate_n_sum(1, -0.5, 300)"
# 100 loops, best of 3: 0.57 usec per loop

def calculate_n_sum_loop(n):
    result = 0
    for i in range(n):
        result += (-0.5) ** i
    return result

# python -m timeit -n 100 -s "import task_1_progression" "task_1_progression.calculate_n_sum_loop(100)"
# 100 loops, best of 3: 25.6 usec per loop

# python -m timeit -n 100 -s "import task_1_progression" "task_1_progression.calculate_n_sum_loop(200)"
# 100 loops, best of 3: 51.1 usec per loop

# python -m timeit -n 100 -s "import task_1_progression" "task_1_progression.calculate_n_sum_loop(300)"
# 100 loops, best of 3: 78.3 usec per loop

# Вывод: 1й алгоритм имеет константную сложность (что и так очевидно =))) и выполняется одинаково быстро для любых
# значениях n, b1, q 2й алгоритм имеет сложность О(n)
# cProfile в данном алгоритме использовать не стал, так как не имеет особого смысла
