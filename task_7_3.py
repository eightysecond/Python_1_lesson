class Cell:
    def __init__(self, value):
        self.value = int(value)

    def __str__(self):
        return f'Результат операции {self.value * "*"}'

    def __add__(self, other):
        return Cell(self.value + other.value)

    def __sub__(self, other):
        if self.value - other.value > 0:
            return Cell(self.value - other.value)
        else:
            return f'Разность количества ячеек двух клеток меньше нуля!'

    def __mul__(self, other):
        return Cell(int(self.value * other.value))

    def __truediv__(self, other):
        return Cell(round(self.value // other.value))


    def make_order(self, cells_in_row):
        row = ''
        for i in range(int(self.value / cells_in_row)):
            row += f'{"*" * cells_in_row} \\n'
        row += f'{"*" * (self.value % cells_in_row)}'
        return row

cell_1 = Cell(12)
cell_2 = Cell(4)
print(cell_1)
print(cell_2)
print(cell_1 + cell_2)
print(cell_1 - cell_2)
print(cell_1 * cell_2)
print(cell_1 / cell_2)
print(cell_1.make_order(5))

