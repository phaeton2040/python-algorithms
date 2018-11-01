# Посчитать четные и нечетные цифры введенного натурального числа. Например, если введено число 34560, то у него 3
# четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).

# Посчитать не используя списки.
# ВЫЗОВ ПРИНЯТ ;)

num = int(input('Введите число: '))
initial_num = num
even_count = 0
odd_count = 0

while num != 0:
    last_digit = num % 10
    num = num // 10
    if last_digit % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

print(f'Четных цифр в числе {initial_num} - {even_count}')
print(f'Нечетных цифр в числе {initial_num} - {odd_count}')

# Если можно использовать списки

# num = input('Введите число: ')
# initial_num = num
# even_count = 0
# odd_count = 0
#
# for digit in num:
#     if int(digit) % 2 == 0:
#         even_count += 1
#     else:
#         odd_count += 1
#
# print(f'Четных цифр в числе {initial_num} - {even_count}')
# print(f'Нечетных цифр в числе {initial_num} - {odd_count}')
