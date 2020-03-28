a = int(input('Введите кол-во км за первый день: '))
b = int(input('Введите желаемый результат в км: '))
days = 1
result_km = a
while result_km < b:
    a = a + 0.1 * a
    days += 1
    result_km += a
print('На', days ,'день спортсмен достиг результата - не менее' , b , 'км')
