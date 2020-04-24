class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'wage': wage, 'bonus': bonus}


class Position(Worker):

    def get_full_name(self):
        return self.name + ' ' + self.surname

    def get_total_income(self):
        return self._income.get("wage") + self._income.get("bonus")


info = Position('Ivan', 'Ivanov', 'mechanic', 15000, 5000)
print(info.get_full_name())
print(info.position)
print(info.get_total_income())
