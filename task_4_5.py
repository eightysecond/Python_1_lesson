from functools import reduce


def my_func(prev_el, el):
    return prev_el * el


print(f'Список четных чисел - {[el for el in range(100, 1001) if el % 2 == 0]}')
print(f'Произведение всех элементов списка - {reduce(my_func, [el for el in range(100, 1001) if el % 2 == 0])}')


"""
Второй вариант, с использованием lambda фун-и
"""

# from functools import reduce

# print(f'произведение - {reduce(lambda x, y: x * y,[el for el in range(1, 10) if el % 2 == 0])}')
