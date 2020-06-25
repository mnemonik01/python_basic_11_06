# homework lesson: 3, task:1



"""
Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.
"""

def div(*args):
    try:
        arg1 = int(input("Введите  делимое"))
        arg2 = int(input("Введите  делитель"))
        res = arg1 / arg2
    except ValueError:
        return 'Ошибка!'
    except ZeroDivisionError:
        return "Неверный делитель. на 0 делить нельзя"

    return res

    '''
    if arg2 != 0:
        return arg1 / arg2
    else:
        print("Делимое должно быть числом")
    '''


print(f'result  {div()}')