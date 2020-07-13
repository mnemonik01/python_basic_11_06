'''
 Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых
 пользователем данных. Например, для указания количества принтеров, отправленных
 на склад, нельзя использовать строковый тип данных.
 Подсказка: постарайтесь по возможности реализовать в проекте «Склад оргтехники»
 максимум возможностей, изученных на уроках по ООП.
 '''


class StoreMashines:

     def __init__(self, name, price, quantity, number_of_lists, *args):
         self.name = name
         self.price = price
         self.quantity = quantity
         self.numb = number_of_lists
         self.my_store_full = []
         self.my_store = []
         self.my_unit = {'Модель принтера': self.name, 'Цена за штуку': self.price, 'Количество': self.quantity}

     def __str__(self):
         return f'{self.name} цена {self.price} количество {self.quantity}'


     def reception(self):
         try:
             unit = input(f'Введите модель принтера ')
             unit_p = int(input(f'Введите цену за единицу '))
             unit_q = int(input(f'Введите количество '))
             unique = {'Модель устройства': unit, 'Цена за ед': unit_p, 'Количество': unit_q}
             self.my_unit.update(unique)
             self.my_store.append(self.my_unit)
             print(f'Текущий список -\n {self.my_store}')
         except:
             return f'Ошибка ввода!'

         print(f'Для выхода нажмите Q, продолжение - Enter')
         q = input(f'---> ')
         if q == 'Q' or q == 'q':
             self.my_store_full.append(self.my_store)
             print(f'Склад -\n {self.my_store_full}')
             return f'Выход'
         else:
             return StoreMashines.reception(self)


class Printer(StoreMashines):
     def to_print(self):
         return f'to print smth {self.numb} times'


class Scanner(StoreMashines):
     def to_scan(self):
         return f'to scan smth {self.numb} times'


class Copier(StoreMashines):
     def to_copier(self):
         return f'to copier smth  {self.numb} times'


unit_1 = Printer('Brother', 4000, 4, 14)
unit_2 = Scanner('Hewlett-Packard', 140, 5, 10)
unit_3 = Copier('Xerox', 6800, 2, 34)
print(unit_1.reception())
print(unit_2.reception())
print(unit_3.reception())
print(unit_1.to_print())
print(unit_3.to_copier())