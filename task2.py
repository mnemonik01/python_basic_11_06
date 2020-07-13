"""
 Реализовать функцию, принимающую несколько параметров,
 описывающих данные пользователя:
 имя, фамилия, год рождения, город проживания, email, телефон.
 Функция должна принимать параметры как именованные аргументы.
 Реализовать вывод данных о пользователе одной строкой.
 """
'''
     name = input('enter name')
     surname = input('enter surname')
     year = int(input('enter year'))
     city = input('enter city')
     email = input('enter email')
     telephone = input('input telephone')
 '''
def my_func (name, surname, year, city, email, telephone):
      return ' '.join([name, surname, year, city, email, telephone])
print(my_func(surname = 'Aminov', name = 'Ruslan', year = '1989', city = 'Sterlitamak', email = 'mail@mail.ru', telephone = '+7-555-55-55'))
