# homework lesson: 3, task:2

"""
Реализовать функцию, принимающую несколько параметров,
описывающих данные пользователя:
имя, фамилия, год рождения, город проживания, email, телефон.
Функция должна принимать параметры как именованные аргументы.
Реализовать вывод данных о пользователе одной строкой.
"""

name = input('Введите  имя')
surname = input('Введите фамилию')
year = int(input('введите год рождения'))
city = input('Введите город')
email = input('Введите ваш почтовый ящик')
telephone = input('Введите телефон')

def my_func (name, surname, year, city, email, telephone):
     return ' '.join([name, surname, year, city, email, telephone])
print(my_func(surname = 'Аминов', name = 'Руслан', year = '1989', city = 'Уфа', email = 'mail@mail.ru', telephone = '8-927-231-00-43'))