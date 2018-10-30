# В программе генерируется случайное целое число от 0 до 100. Пользователь должен его отгадать не более чем за 10
# попыток. После каждой неудачной попытки должно сообщаться, больше или меньше загаданного введенное пользователем
# число. Если за 10 попыток число не отгадано, то вывести его.

import random

max_tries = 10
try_number = 1
success = False
random_number = random.randint(0, 100)

print('Угадайти число от 0 до 100!')

while try_number <= max_tries:
    guess = int(input(f'{try_number} попытка: '))

    if guess == random_number:
        print('Угадали :)')
        success = True
        break
    else:
        try_number += 1

        if guess > random_number:
            print('Не угадали :( Возьмите меньше')
        else:
            print('Не угадали :( Возьмите больше')
        continue

if not success:
    print(f'Было загадано число - {random_number}')

print('Конец')
