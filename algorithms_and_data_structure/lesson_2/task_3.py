'''Сформировать из введенного числа обратное по
порядку входящих в него цифр и вывести на экран.
'''

def var_1():
    num = int(input('введите число --> '))
    new_num = ''
    while num:
        new_num += str(num // 10 ** 0 % 10)
        num = num // 10
    return print(f'ваше число --> {new_num}')

var_1()