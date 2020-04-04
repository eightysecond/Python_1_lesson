name = input('enter name ')
surname = input('enter surname ')
year = input('enter year ')
city = input('enter city ')
email = input('enter email ')
phone = input('enter phone ')


def my_list(name, surname, year, city, email, phone):
    return ' '.join([name, surname, year, city, email, phone])


print(my_list(name, surname, year, city, email, phone))

