from itertools import count, cycle

for el in count(int(input('Введите начальное число '))):
    if el > 10:
        break
    else:
        print(el)

c = 0
my_list = ['A', 'BC', 'DEF', 1, 2, 3]
for el in cycle(my_list):
    if c > 5:
        break
    else:
        print(el)
        c += 1
