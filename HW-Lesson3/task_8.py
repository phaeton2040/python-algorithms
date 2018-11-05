# Матрица 5x4 заполняется вводом с клавиатуры, кроме последних элементов строк. Программа должна вычислять сумму
# введенных элементов каждой строки и записывать ее в ее последнюю ячейку. В конце следует вывести полученную матрицу.

ROWS = 4
COLUMNS = 4

matrix = []

row = 0
while row < ROWS:
    matrix.append([])
    col = 0
    while col < COLUMNS:
        matrix[row].append(int(input(f'Введите {col + 1} столбец {row + 1} ряда: ')))
        col += 1
    # допишем сумму элементов строк в последний столбец
    row_sum = 0
    for i in matrix[row]:
        row_sum += i
    matrix[row].append(row_sum)
    row += 1

# выводим полученную матрицу
for row in matrix:
    for col in row:
        print(col, end=', ')
    print('')
