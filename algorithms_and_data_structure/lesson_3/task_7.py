'''В одномерном массиве целых чисел определить
 два наименьших элемента. Они могут быть как равны
 между собой (оба минимальны), так и различаться.'''

import random
a = [random.randint(0,100) for i in range(500)]
print(a)
min_1 = a[0]
min_2 = a[0]
index = 0
for i,j in enumerate(a):
    if j < min_1:
        min_1 = j
        index = i

del a[index]
for i,j in enumerate(a):
    if j < min_2:
        min_2 = j
        index = i


print(min_1, min_2)