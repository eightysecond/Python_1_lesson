def result(arg_1, arg_2):
    try:
        div = arg_1 / arg_2
    except ZeroDivisionError:
        return 'division by zero'
    return div


print(f'Result - {result(int(input("enter 1 number: ")), int(input("enter 2 number: ")))}')
