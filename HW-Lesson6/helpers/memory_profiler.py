# Декоратор для профилирования использования памяти переменными декорируемой функции

import sys


def profiler(func=None, verbose=False):
    if func:
        return _Profiler(func, verbose)
    else:
        def wrapper(func):
            return _Profiler(func, verbose)
        return wrapper


class _Profiler(object):
    def __init__(self, func, verbose):
        self._locals = {}
        self.func = func
        self.verbose = verbose

    def _count_size(self, name, x, level=0):
        size = sys.getsizeof(x)

        if self.verbose:
            print('\t' * level, f'Переменная - {name}, тип {type(x)}: {sys.getsizeof(x)}')
        if hasattr(x, '__iter__'):
            if hasattr(x, 'items'):
                for key, value in x.items():
                    size += self._count_size(f'{key}-ключ', key, level + 1) or 0 # не самый красивый хак. С удовольствием приму совет, как можно сделать по другому =)
                    size += self._count_size(f'{key}-значение', value, level + 1) or 0
                return size
            elif not isinstance(x, str):
                i = 0
                for item in x:
                    size += self._count_size(f'{i + 1}-й элемент', item, level + 1) or 0
                    i += 1
                return size
        else:
            return size

    def __call__(self, *args, **kwargs):
        def tracer(frame, event, arg):
            if event == 'return':
                self._locals = frame.f_locals.copy()

        sys.setprofile(tracer)
        try:
            res = self.func(*args, **kwargs)
        finally:
            total = 0
            for key, value in self.locals.items():
                total += self._count_size(key, value) or 0

            print('-' * 40)
            print(f'Всего памяти выделено: {total} bytes')
            sys.setprofile(None)
        return res

    @property
    def locals(self):
        return self._locals

