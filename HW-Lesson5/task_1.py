# Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4 квартала для каждого
# предприятия. Программа должна определить среднюю прибыль (за год для всех предприятий) и вывести наименования
# предприятий, чья прибыль выше среднего и отдельно вывести наименования предприятий, чья прибыль ниже среднего.

from collections import namedtuple, defaultdict


Firm = namedtuple('Firm', 'name, revenue')

quantity = int(input('Введите кол-во предприятий: '))
firms = []
revenues = []

for i in range(quantity):
    name = input(f'Предприятие {i + 1}: ')

    q1 = float(input('Прибыль 1й квартал: '))
    q2 = float(input('Прибыль 2й квартал: '))
    q3 = float(input('Прибыль 3й квартал: '))
    q4 = float(input('Прибыль 4й квартал: '))

    firm = Firm(name, q1 + q2 + q3 + q4)
    firms.append(firm)
    revenues.append(firm.revenue)

total_avg_revenue = sum(revenues) / len(revenues)

print(f'Средняя прибыль по всем предприятиям за год: {total_avg_revenue}')

firms_stat = defaultdict(list)
for firm in firms:
    if firm.revenue < total_avg_revenue:
        firms_stat['less'].append((firm.name, firm.revenue))
    else:
        firms_stat['more'].append((firm.name, firm.revenue))

print('Предприятия, имеющие прибыль ниже среднего: ')
print(firms_stat['less'])

print('Предприятия, имеющие прибыль выше среднего: ')
print(firms_stat['more'])
