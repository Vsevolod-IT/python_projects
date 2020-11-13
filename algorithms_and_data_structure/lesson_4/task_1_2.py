# Проанализировать скорость и сложность одного любого алгоритма из разработанных
# в рамках домашнего задания первых трех уроков.


# Берется задание из lesson 3 task_4:
# Определить, какое число в массиве встречается чаще всего


import cProfile
import random

def func_1(n):
    # создание массива
    a = [random.randint(0,10) for i in range(n)]

    # создание ключей для словаря (ключ - элемент который имеется в массиве)
    # ключ во время итераций будет всегда акуален для поиска в цикле
    key = set(a)

    # создание словаря с ключами(элемаентами в массиве) с значением которое потом сможем менять
    res = {}
    for i in key:
        res[i] = 0

    # благодаря словарю res{} у нас есть счетчик для каждого элемента
    # который мы теперь обнавляем при каждом вхождении  элемента
    for i in a:
        if i in key:
            res[i] += 1

    # находим максимальное значение в словаре
    max = 0
    for i in res.values():
        if i > max:
            max = i

    # ищем все элементы удовлетворяющие max и заносим в финальный словарь
    result = {}
    for k, v in res.items():
        if v == max:
            result[k] = v


    return res,result

#  python -m timeit -n 1000 -s "import task_1_2" "task_1_2.func_1(100)" n = 100
# 1000 loops, best of 5: 114 usec per loop

# python -m timeit -n 1000 -s "import task_1_2" "task_1_2.func_1(1000)" n = 1000
# 1000 loops, best of 5: 1.11 msec per loop

#  python -m timeit -n 1000 -s "import task_1_2" "task_1_2.func_1(10000)"
#  1000 loops, best of 5: 12.3 msec per loop

# cProfile.run('func_1(10000)')
# 1    0.000    0.000    0.000    0.000 task_1_2.py:12(func_1) n = 100
# 1    0.000    0.000    0.002    0.002 task_1_2.py:12(func_1) n = 1000
# 1    0.002    0.002    0.036    0.036 task_1_2.py:12(func_1) n = 10000


# 1 - используем метод list.count()
# 2 - заменим словарь на список, теперь нечетный элемент
#     это ключ а четный кол-во повторений


def func_2(n):
    # создание массива
    a = [random.randint(0,10) for i in range(n)]

    # 1 - используем метод list.count()
    # 2 - заменим словарь на список, теперь нечетный элемент
    #     это ключ а четный кол-во повторений
    key = set(a)
    res = []
    for i in key:
        res.append(i)
        count = a.count(i)
        res.append(count)
    s = max(res[1::2])
    d = res.index(s) - 1
    d = res[d]

    return d, s
# python -m timeit -n 1000 -s "import task_1_2" "task_1_2.func_2(100)" n = 100
# 1000 loops, best of 5: 154 usec per loop

# python -m timeit -n 1000 -s "import task_1_2" "task_1_2.func_2(1000)" n = 1000
# 1000 loops, best of 5: 1.36 msec per loop

# python -m timeit -n 1000 -s "import task_1_2" "task_1_2.func_2(10000)" n = 10000
# 1000 loops, best of 5: 13.9 msec per loop

cProfile.run('func_2(10000)')
# 1    0.000    0.000    0.000    0.000 task_1_2.py:66(func_2) n = 100
# 1    0.000    0.000    0.004    0.004 task_1_2.py:66(func_2) n = 1000
# 1    0.000    0.000    0.033    0.033 task_1_2.py:66(func_2) n = 10000
