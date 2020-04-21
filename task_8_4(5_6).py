class Office_automation:
    def __init__(self, name, quantity, price, *args):
        self.name = name
        self.quantity = quantity
        self.price = price
        self.store_full = []
        self.store = []
        self.my_unit = {'Модель устройства': self.name, 'Количество': self.quantity, 'Стоимость': self.price}

    def __str__(self):
        return f'{self.name}, количество - {self.quantity}, цена - {self.price}'

    def reception(self):
        try:
            unit = input(f'Введите наименование ')
            unit_p = int(input(f'Введите стоимость единицы техники '))
            unit_q = int(input(f'Введите количество передаваемой техники '))
            unique = {'Модель устройства': unit, 'Количество': unit_q, 'Стоимость': unit_p}
            self.my_unit.update(unique)
            self.store.append(self.my_unit)
            print(f'Текущий список техники \n {self.store}')
        except:
            return f'Ошибка ввода'

        print(f'Q - выход, Enter - продолжить')
        q = input(f'==> ')
        if q == 'Q' or q == 'q':
            self.store_full.append(self.store)
            print(f'На складе \n {self.store_full}')
            return f'Выход'
        else:
            return Office_automation.reception(self)


class Printer(Office_automation):
    def get_print(self):
        return f'Вывод на печать'


class Scaner(Office_automation):
    def get_scan(self):
        return f'Сканирование документа'


class Copier(Office_automation):
    def get_copy(self):
        return f'Ксерокопия документа'


unit1 = Printer('Hewlett-Packard', 20, 5000)
unit2 = Scaner('Canon', 10, 2500)
unit3 = Copier('Xerox', 15, 10000)
print(unit1.reception())

