class ComplexNumb:
    def __init__(self, a, b, *args):
        self.a = a
        self.b = b
        self.z = 'a+b*i'

    def __add__(self, other):
        print(f'Сумма двух комлексных чисел равна ')
        return f'z = {self.a + other.a} + {self.b + other.b}*i'

    def __mul__(self, other):
        print(f'Произведение двух комлексных чисел равно ')
        return f'z = {self.a * other.a - (self.b * other.b)} + {self.a * other.b + (self.b * other.a)}*i'

    def __str__(self):
        return f'z={self.a} + {self.b}*i'


z1 = ComplexNumb(1, 2)
z2 = ComplexNumb(3, 4)
print(z1)
print(z1 + z2)
print(z1 * z2)
