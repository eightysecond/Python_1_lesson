my_f = open('task_51.txt', 'w')
line = input('Введите текст: \n')
while True:
    my_f.writelines(line)
    line = input('Введите текст: \n')
    if not line:
        break

my_f.close()
my_f = open('task_51.txt', 'r')
print(my_f.readlines())
my_f.close()
