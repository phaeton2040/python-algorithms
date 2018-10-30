# Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран. Например,
# если введено число 3486, то надо вывести число 6843.

num = int(input('Введите число: '))
reversed_num = ''

while num != 0:
    last_digit = num % 10
    num = num // 10
    reversed_num = f'{reversed_num}{last_digit}'

print(reversed_num)
