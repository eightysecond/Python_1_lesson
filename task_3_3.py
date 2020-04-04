def my_func(arg_1, arg_2, arg_3):
    if arg_1 > arg_3 and arg_2 > arg_3:
        return arg_1 + arg_2
    elif arg_2 < arg_1 < arg_3:
        return arg_1 + arg_3
    else:
        return arg_2 + arg_3


print(f'Result - {my_func(int(input("enter 1 numb ")), int(input("enter 2 numb ")), int(input("enter 3 numb ")))}')