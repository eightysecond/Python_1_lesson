from sys import argv

time, salary, award = argv
try:
    time = int(time)
    salary = int(salary)
    award = int(award)
    result = time * salary + award
    print(f'Заработная плата = {result}')
except ValueError:
    print('Not a number')

