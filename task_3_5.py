def my_sum():
    sum_res = 0
    ex = False
    while ex == False:
        number = input('Input numbers or Q for quit - ').split()

        res = 0
        for i in range(len(number)):
            if number[i] == 'q' or number[i] == 'Q':
                ex = True
                break
            else:
                res = res + int(number[i])
        sum_res = sum_res + res
        print(f'Current sum is {sum_res}')
    print(f'Your final sum is {sum_res}')


my_sum()
