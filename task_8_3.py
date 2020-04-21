class Error:
    def __init__(self, *args):
        self.my_list = []

    def my_input(self):
        while True:
            try:
                val = int(input('Вводите числа: '))
                self.my_list.append(val)
                print(f'Текущий список - {self.my_list} ')
            except:
                print(f'Введен элемент типа строка или булево')
                option = input(f'Попробовать ещё раз? Y/N ')

                if option == 'Y' or option == 'y':
                    print(try_except.my_input())
                elif option == 'N' or option == 'n':
                    print(f'Вы вышли')
                else:
                    return f'Вы вышли'


try_except = Error()
print(try_except.my_input())
