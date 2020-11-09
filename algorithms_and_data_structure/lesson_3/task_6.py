''' В одномерном массиве найти сумму элементов, находящихся между минимальным
 и максимальным элементами. Сами минимальный и максимальный элементы в сумму не включать.'''

import random
a = [random.randint(0,100) for i in range(50)]

index_min = 0
index_max = 0
r_min_2 = a[0]
r_max_2 = a[0]
for i,k in enumerate(a):
    if r_max_2 < k:
       r_max_2 = k
       index_max = i
    elif k < r_min_2:
        r_min_2 = k
        index_min = i

print(r_min_2,r_max_2)
print(a)
sum_1 = 0
if index_max < index_min:
    index_max -= 1
    sum_1 += index_max
    index_max -= 1
    for i in (a[index_max:index_min:-1]):
        sum_1 += i

else:
    index_min += 1
    sum_1 += index_min
    index_max += 1
    for i in (a[index_min:index_max]):
        sum_1 += i
print(sum_1)
