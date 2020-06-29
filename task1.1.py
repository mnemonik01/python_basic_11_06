def sal():
    try:
        time = float(input('Отработанное время '))
        salary = int(input('Часовая ставка '))
        bonus = int(input('Премия '))
        res = time * salary + bonus
        print(f'общая зарплата  {res}')
    except ValueError:
        return print('Not a number')
sal()