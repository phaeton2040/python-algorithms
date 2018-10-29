# Пользователь вводит номер буквы в алфавите. Определить, какая это буква.

letter_a_code = 96
letter_z_code = 122

letter_num = int(input('Введите номер буквы английского алфавита: ')) + letter_a_code

if letter_a_code <= letter_num <= letter_z_code:
    print(f'Буква на выбранном месте: {chr(letter_num)}')
else:
    print(f'Буквы на выбранном месте не существует')
