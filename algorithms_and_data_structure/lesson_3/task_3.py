'''В массиве случайных целых чисел поменять
местами минимальный и максимальный элементы.'''
import random
a = [random.randint(0,100) for i in range(100)]

# 1 вариант
# a.sort()
# r_min, r_max = a[0], a[-1]
# print(r_min,r_max)

# 2 вариант не зависит от сортированности списка
r_min_2 = a[0]
r_max_2 = a[0]
for i,k in enumerate(a):
    if r_max_2 < k:
       r_max_2 = k
    elif k < r_min_2:
       r_min_2 = k

print(r_min_2,r_max_2)