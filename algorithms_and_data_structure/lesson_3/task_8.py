'''Матрица 5x4 заполняется вводом с клавиатуры, кроме последних
 элементов строк. Программа должна вычислять сумму введенных элементов
 каждой строки и записывать ее в последнюю ячейку строки.
 В конце следует вывести полученную матрицу.
'''
import random
matrix = [[int(input('введите число: ')) for _ in range(5)] for _ in range(4)]




for line in matrix:
    sum_line = 0
    for line, item in enumerate(line):
        sum_line += item
        print(f'{item:>4}', end=' ')
    print(f'   | {sum_line}')


