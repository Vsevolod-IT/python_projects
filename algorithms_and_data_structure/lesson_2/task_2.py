'''Посчитать четные и нечетные цифры введенного натурального
числа. Например, если введено число 34560, в нем 3 четные цифры
(4, 6 и 0) и 2 нечетные (3 и 5).'''

def var_1(num): # начиная с 20 до 25 знаков функция тормозит, если больше то работает вечно)))
    even, odd =  0, 0
    num = int(num)
    while num:
        checking_num = num // 10 ** 0 % 10
        if checking_num % 2 ==0:
            even += 1
        else:
            odd += 1
        num = num // 10
        var_1(num)
    return f'четных:{even}, нечетных:{odd}'


def var_2(num):
    even, odd = 0, 0
    num = str(num)
    for i,k in enumerate(num):
        if int(k) % 2 == 0:
            even += 1
        else:
            odd += 1
    return print(f'четных: {even}, нечетных: {odd}')

def var_3(num):
    even, odd = 0, 0
    digit = '2,4,6,8'
    for i in num:
        if i in digit:
            even += 1
        else:
            odd += 1
    return print(f'четных:{even}, нечетных:{odd}')




num = input('введите число --> ')
print(var_1(num))
var_2(num)
var_3(num)