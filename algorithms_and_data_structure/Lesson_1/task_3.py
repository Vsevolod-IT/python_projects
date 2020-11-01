'''Написать программу, которая генерирует в указанных пользователем границах:
a. случайное целое число,
b. случайное вещественное число,
c. случайный символ.
Для каждого из трех случаев пользователь задает свои границы диапазона. Например,
 если надо получить случайный символ от 'a' до 'f', то вводятся эти символы. Программа
 должна вывести на экран любой символ алфавита от 'a' до 'f' включительно.'''

import random

num_1,num_2 = map(int,input('Введите диапазон чисел для выбора целого числа -->').split())
real_num_1, real_num_2 = map(int,input('Введите диапазон чисел для выбора вещественного числа -->').split())
letter_1,letter_2 = map(str,input('Введите диапазон для выбора буквы (s z) -->').split())

num_2,real_num_2 = num_2 +1, real_num_2 + 1
letter_1,letter_2 = ord(letter_1), ord(letter_2) + 1
number = random.randint(num_1,num_2)
real_number = random.uniform(real_num_1, real_num_2)
letter = chr(random.randint(letter_1, letter_2))

print(f'целое число: {number}\nвещественное число: {real_number}\nбуква: {letter}')