''' Найти максимальный элемент среди минимальных элементов столбцов матрицы.'''

import random

# создание массива
matrix = [[random.randint(1,10) for _ in range(5)] for _ in range(4)]

# распечатаем матрицу для наглядности
for line in matrix:
    for line, item in enumerate(line):
        print(f'{item:>4}', end=' ')
    print()

# список с минимальными значениями в столбцах
min_column = []

for k in range(len(matrix[0])):

    min = matrix[0][k]              # записываем первый элемент столбца
    min_column.append(min)
    for i,j in enumerate(matrix):

        if matrix[i][k] < min:
            del min_column[k]
            min_column.append(matrix[i][k])
            min = matrix[i][k]

print(min_column)

high_min = min_column[0]
for i in min_column:
    if i > high_min:
        high_min = i

print(high_min)