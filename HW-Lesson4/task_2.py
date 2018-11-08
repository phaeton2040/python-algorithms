import cProfile
import itertools


def get_prime(n):
    prime_list = [2]
    num = 3
    while len(prime_list) < n:
        for p in prime_list:
            if num % p == 0:
                break
        else:
            prime_list.append(num)
        # очевидный вариант оптимизации - пропускать нечетные числа
        num += 2
    return prime_list[-1]

# python -m timeit -n 100 -s "import task_2" "task_2.get_prime(50)"
# 100 loops, best of 3: 113 usec per loop

# python -m timeit -n 100 -s "import task_2" "task_2.get_prime(100)"
# 100 loops, best of 3: 371 usec per loop

# python -m timeit -n 100 -s "import task_2" "task_2.get_prime(150)"
# 100 loops, best of 3: 807 usec per loop

# cProfile.run('get_prime(250)') 1    0.003    0.003    0.003    0.003 task_2.py:5(get_prime)
# cProfile.run('get_prime(500)') 1    0.010    0.010    0.010    0.010 task_2.py:5(get_prime)
# cProfile.run('get_prime(750)') 1    0.022    0.022    0.022    0.022 task_2.py:5(get_prime)

# поскольку в этот раз всего 2 задания, я почитал про решето Эротосфена и нашел интересные варианты реализации этого
# алгоритма.
# В нашем ДЗ необходимо модифицировать алгоритм так, чтобы он возвращал простое число n-е по счету
# Алгоритм ниже не "прокалывает дыры" в доске (заполнение нулями), а хранит словарь вида:
# {[число]: [первый простой множитель]}, что тоже является аналогом мемоизации с нулями, рассмотренной на уроке.
# Также у меня было время разобраться с работой генераторов в python
# и решение ниже я привожу с учетом приобретенных знаний ;)


def primes():
    """Генератор последовательности случайных чисел"""
    sieve = {}
    yield 2
    for num in itertools.count(3, 2):
        # мы можем удалить из словаря текущий элемент, так как он гарантированно не понадобится в будущем
        prime_factor = sieve.pop(num, None)
        if prime_factor is None:
            # если num не в решете (sieve), то пропускаем его
            yield num
            # num * num - гарантированно не простое число, можем занести его в решето
            sieve[num*num] = num
        else:
            # если мы попали сюда, значит мы наткнулись на не простое число
            # в этом случае мы должны добавить в наше решето новый элемент, так как текущий мы удалили
            # поскольку num - элемент из последовательности нечетных чисел,
            # а prime_factor - первый простой множитель, то следующее нечетное число:
            # num + prime_factor можно занести в решето, как заведомо не простое
            x = num + prime_factor
            while x in sieve or x % 2 == 0:
                x += prime_factor
            sieve[x] = prime_factor


def get_prime_optimized(n):
    for i, p in enumerate(primes(), 1):
        if i == n:
            return p

# python -m timeit -n 100 -s "import task_2" "task_2.get_prime_optimized(50)"
# 100 loops, best of 3: 62.1 usec per loop

# python -m timeit -n 100 -s "import task_2" "task_2.get_prime_optimized(100)"
# 100 loops, best of 3: 155 usec per loop

# python -m timeit -n 100 -s "import task_2" "task_2.get_prime_optimized(150)"
# 100 loops, best of 3: 261 usec per loop

# cProfile.run('get_prime_optimized(250)')
# 251    0.000    0.000    0.001    0.000 task_2.py:43(primes)
#   1    0.000    0.000    0.001    0.001 task_2.py:67(get_prime_optimized)
# cProfile.run('get_prime_optimized(500)')
# 501    0.001    0.000    0.002    0.000 task_2.py:43(primes)
#   1    0.000    0.000    0.002    0.002 task_2.py:67(get_prime_optimized)
# cProfile.run('get_prime_optimized(750)')
# 751    0.002    0.000    0.002    0.000 task_2.py:43(primes)
#   1    0.000    0.000    0.003    0.003 task_2.py:67(get_prime_optimized)

# Вывод очевиден =)
