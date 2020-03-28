take = int(input('Введите сумму выручки: '))
cost = int(input('Введите сумму издержек: '))
profit = take - cost
rentability = profit / take

if take < cost:
    print('Финансовый результат работы - убыток')
else:
    print('Финансовый результат работы - прибыль.', 'Рентабельность фирмы составила:', rentability, '%')

firm_size = int(input('Введите колличество сотрудников: '))
rent_human = profit / firm_size
print('Прибыль фирмы в расчете на одного сотрудника, составила: ', rent_human, 'руб.')

