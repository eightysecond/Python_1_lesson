sec = int(input('Введите колличество секунд: '))
h = sec // 3600
m = sec // 60
s = sec % 60
print('{0:=02}:{1:=02}:{2:=02}'.format(h, m, s))