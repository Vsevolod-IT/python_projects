'''Посчитать, сколько раз встречается определенная цифра в
 введенной последовательности чисел. Количество вводимых чисел
 и цифра, которую необходимо посчитать, задаются вводом с клавиатуры.'''

def sep(data):
    m = int(data)
    num = str(m // 10 ** 0 % 10)
    data = str(m // 10)
    return num, data

def func(data):
    res = ''
    checked = ''
    for i in data:
        num,data = sep(data)
        if (num in data) and (num not in checked):
            count = 1
            for _,k in enumerate(data):
                if num == k:
                   count += 1
            res += f'число {num} : встречается {count} раз \n'
        checked += f'{num}'
    return print(res)

data = input('введите число, программа подсчитает цифры которые будут повторяться --> ')

print(func(data))
