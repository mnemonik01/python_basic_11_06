def insert_sum(*args):
    result = 0
    exit_flag = False
    for itm in args:
        try:
            result += float(itm)
        except ValueError as e:
            if itm == 'q':
                exit_flag = not exit_flag
                break

    return result, exit_flag


user_exit = False
user_sum = 0
while not user_exit:
    user_input = input('введите числа через пробел\n').split(' ')
    result_summ, user_exit = insert_sum(*user_input)
    user_sum += result_summ
    print(f'сумма: {user_sum}')