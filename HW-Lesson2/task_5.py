# Вывести на экран коды и символы таблицы ASCII, начиная с символа под номером 32 и заканчивая 127-м включительно.
# Вывод выполнить в табличной форме: по десять пар «код-символ» в каждой строке.
START = 32
END = 128

for i in range(START, END):
    if (i - START) % 10 == 0 and i > START:
        print('\n')
    print(f'({i}, \'{chr(i)}\')', end=', ')