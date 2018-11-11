# Написать программу сложения и умножения двух шестнадцатеричных чисел. При этом каждое число представляется как
# массив, элементы которого это цифры числа.

from HexNumber import HexNumber

# к сожалению, на больших числах очень тормозит, не получается оптимизировать
a = HexNumber(input('Введите первое число (a): '))
b = HexNumber(input('Введите второе число (b): '))
c = HexNumber(input('Введите третье число (c): '))


print(f'a + b = {a + b}')
print(f'a + b + c = {a + b + c}')
print(f'a * b = {a * b}')
print(f'a * b * c = {a * b * c}')


def test(a, b):
    a16 = int(a.num, base=16)
    b16 = int(b.num, base=16)
    c16 = int(c.num, base=16)
    assert (a + b) == str(hex(a16 + b16))[2:].upper(), 'Result mismatch'
    assert (a + b + c) == str(hex(a16 + b16 + c16))[2:].upper(), 'Result mismatch'
    assert (a * b) == str(hex(a16 * b16))[2:].upper(), 'Result mismatch'
    assert (a * b * c) == str(hex(a16 * b16 * c16))[2:].upper(), 'Result mismatch'
    print('OK!')


test(a, b)
