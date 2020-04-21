class Division:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    @staticmethod
    def div(a, b):
        try:
            res = a / b
        except ZeroDivisionError:
            return f'Division zero'
        else:
            return f'Результат деления - {res}'


c = Division(15,3)
print(Division.div(15, 3))
print(c.div(10, 0))
