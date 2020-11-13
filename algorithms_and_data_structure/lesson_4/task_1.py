# Проанализировать скорость и сложность одного любого алгоритма из разработанных
# в рамках домашнего задания первых трех уроков.


# Берется задание из lesson 3 task_1:
# В диапазоне натуральных чисел
# от 2 до 99 определить, сколько из них кратны
#  каждому из чисел в диапазоне от 2 до 9.

import cProfile


# для задания мы будем увеличивать диапазон натуральных чисел
# а также заключим каждый алгоритм как функцию
# для облегчения анализа скорости

def first_alg(n):
    b = [0]*8
    for i in range(2,n):
        for j in range(2,10):
            if i%j == 0:
                b[j-2] += 1

    res = {}
    i = 0
    while i < len(b):
        res[i+2] = b[i]
        i += 1
    return res

# python -m timeit -n 1000 -s "import task_1" "task_1.first_alg(100)" n = 100
# 1000 loops, best of 5: 81.2 usec per loop                           число операций = 1060

# python -m timeit -n 1000 -s "import task_1" "task_1.first_alg(1000)" n = 1000
# 1000 loops, best of 5: 843 usec per loop                             число операций = 10805

# python -m timeit -n 1000 -s "import task_1" "task_1.first_alg(10000)" n = 10000
# 1000 loops, best of 5: 8.65 msec per loop                             число операций = 108266

# cProfile.run('first_alg(10000)')
# 1    0.000    0.000    0.000    0.000 task_1.py:16(first_alg) n = 100
# 1    0.001    0.001    0.001    0.001 task_1.py:16(first_alg) n = 1000
# 1    0.013    0.013    0.013    0.013 task_1.py:16(first_alg) n = 10000


# переделаем фунцию добавив проверки if  и тем самым сократив число циклов

def new_alg (n):

    a = [i for i in range(2,n)]
    res = dict(zip([i for i in range(2,10)], [0]*8))


    for i in a:
        if i % 2 == 0:
            res[2] += 1

            if i % 4 == 0:
                res[4] += 1

                if i % 8 == 0:
                    res[8] += 1

            elif i % 6 == 0:
                res[6] += 1

        elif i % 3 == 0:
            res[3] += 1

            if i % 9 == 0:
                res[9] += 1

        elif i % 5 == 0:
            res[5] += 1

        else:
            res[7] += 1

    return res

# python -m timeit -n 1000 -s "import task_1" "task_1.new_alg(100)" n = 100
# 1000 loops, best of 5: 34.6 usec per loop                         число операций = 246

# python -m timeit -n 1000 -s "import task_1" "task_1.new_alg(1000)" n = 1000
# 1000 loops, best of 5: 342 usec per loop                           число операций = 2508

# python -m timeit -n 1000 -s "import task_1" "task_1.new_alg(10000)" n = 10000
# 1000 loops, best of 5: 3.71 msec per loop                           число операций = 25133

#cProfile.run('new_alg(10000)')
# 1    0.000    0.000    0.000    0.000 task_1.py:47(new_alg) n = 100
# 1    0.001    0.001    0.001    0.001 task_1.py:47(new_alg) n = 1000
# 1    0.003    0.003    0.004    0.004 task_1.py:47(new_alg) n = 10000

