my_list = [7, 5, 3, 3, 2]
print(f'Текущий рейтинг - {my_list}')
number = int(input('Введите число, 111 для выхода: '))
while number != 111:
    for i in range(len(my_list)):
        if my_list[i] == number:
            my_list.insert(i + 1, number)
            break
        elif my_list[0] < number:
            my_list.insert(0, number)
        elif my_list[-1] > number:
            my_list.append(number)
        elif my_list[i] > number and my_list[i + 1] < number:
            my_list.insert(i + 1, number)
    print(f"Итоговый рейтинг - {my_list}")
    number = int(input('Введите число: '))