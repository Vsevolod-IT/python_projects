#1. Пользователь вводит данные о количестве предприятий, их наименования и прибыль
#     за четыре квартала для каждого предприятия. Программа должна определить среднюю прибыль
#   (за год для всех предприятий) и отдельно вывести наименования предприятий, чья прибыль выше
#   среднего и ниже среднего.

from collections import defaultdict


def getDict():
    res = defaultdict(list)
    while (True):
        print('Enter company_name (empty enter - exit)')
        company = input('-->')
        if company == '':
            break
        print('Enter each qurt profit')

        profit = list(map(int,input().split()))
        res[company] = profit
    return res


d = getDict()
print(d)

mean = 0
for i in d.keys():
    work_box = d[i]
    m_year = sum(work_box) // 4
    d[i] = m_year
    mean += m_year

count_company = len(d.keys())
mean = mean // count_company
for i in d.keys():
    if d[i] > mean:
        print(f'{d[i]}  above the average --> {mean}\n')
    elif d[i] < mean:
        print(f'{d[i]}  below the average --> {mean}\n')
print()


