from collections import deque

# про "наследоваться от Counter" это я, конечно, фигню сказал,
# Counter все так не для этого. Тем не менее, логично было бы объеденить
# алгоритмы сложения и умножения в собственную структуру.
# Как например Vector2, Vector3 в игровых движках
# Ниже написаны необходимые алгоритмы, а также переопределены операторы + и *
# Хотел также перепопределить операторы сравнения, но не хватило времени
# Также было обидно узнать, что в python нет private методов
class HexNumber(object):
    _hex_base = {
        '0': 0,
        '1': 1,
        '2': 2,
        '3': 3,
        '4': 4,
        '5': 5,
        '6': 6,
        '7': 7,
        '8': 8,
        '9': 9,
        'A': 10,
        'B': 11,
        'C': 12,
        'D': 13,
        'E': 14,
        'F': 15
    }

    num: str

    def __init__(self, num):
        self.num = str(num).upper()

    # я разбил алгоритмы сложения и умножения на 2 метода
    # 1-й метод занимается сложением/умножением однозначных чисел,
    # 2-й метод использует 1-й для реализации сложения/умножения "в столбик"
    def _sum_primitives(self, a: str, b: str) -> (str, int):
        if len(a) > 1 or len(b) > 1:
            raise ValueError('Method accepts only primitive hex numbers!')

        if a not in self._hex_base.keys() or b not in self._hex_base.keys():
            raise ValueError('Invalid symbols in a given number')

        a_shift, b_shift = self._hex_base[a], self._hex_base[b]

        hex_sum_table = deque([(i, 0) for i in self._hex_base.keys()], maxlen=16)

        extension = [(i, 1) for i in list(self._hex_base.keys())[:a_shift]]
        hex_sum_table.extend(extension)

        return hex_sum_table[b_shift]

    # Данный метод реализует алгоритм сложения типа "в столбик"
    def _sum(self, a: str, b: str) -> str:
        length = max(len(a), len(b))
        a = deque(''.join(a).zfill(length))
        b = deque(''.join(b).zfill(length))

        a.reverse()
        b.reverse()

        result = deque()

        # переменная для обработки "1 в уме"
        carry = 0
        for i in range(length):
            member_sum = self._sum_primitives(a[i], b[i])
            ext = self._sum_primitives(member_sum[0], str(carry))
            result.extendleft(ext[0])
            carry = max(ext[1], member_sum[1])

        if carry:
            result.extendleft([str(carry)])

        return ''.join(result)

    def _multiply_primitives(self, a: str, b: str) -> str:
        result = a
        inc = '1'
        while inc != b:
            result = self._sum(a, result)
            inc = self._sum(inc, '1')

        return result

    # Алгоритм умножения типа "в столбик"
    def _multiply(self, a: str, b: str) -> str:
        if len(a) < len(b):
            a, b = b, a
        length = min(len(a), len(b))

        result = '0'
        for i in range(length):
            result = self._sum(result, f'{self._multiply_primitives(a, b[i])}{"0" * (length - i - 1)}')

        return result

    def __radd__(self, other):
        return self._sum(self.num, str(other))

    def __add__(self, other):
        return self._sum(self.num, other.num)

    def __mul__(self, other):
        return self._multiply(self.num, other.num)

    def __rmul__(self, other):
        return self._multiply(self.num, str(other))
