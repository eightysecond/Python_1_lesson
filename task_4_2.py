my_list = [2, 5, 10, 11, 20, 4, 66, 3]
new_list = [el for num, el in enumerate(my_list) if my_list[num - 1] < my_list[num]]
print(f'исходный список {my_list}')
print(f'Новый список {new_list}')
