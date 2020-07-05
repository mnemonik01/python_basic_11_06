'''
 Реализуйте базовый класс Car. У данного класса должны быть
 следующие атрибуты: speed, color, name, is_police (булево).
 А также методы: go, stop, turn(direction), которые должны
 сообщать, что машина поехала, остановилась, повернула (куда).
 Опишите несколько дочерних классов: TownCar, SportCar, WorkCar,
 PoliceCar. Добавьте в базовый класс метод show_speed, который
 должен показывать текущую скорость автомобиля. Для классов TownCar
 и WorkCar переопределите метод show_speed.
 При значении скорости свыше 60 (TownCar) и 40 (WorkCar)
 должно выводиться сообщение о превышении скорости.
 Создайте экземпляры классов, передайте значения атрибутов.
 Выполните доступ к атрибутам, выведите результат.
 Выполните вызов методов и также покажите результат.
 '''


class Car:
     # atributes
     def __init__(self, speed, color, name, is_police):
         self.speed = speed
         self.color = color
         self.name = name
         self.is_police = is_police

     # methods
     def go(self):
         return f'{self.name} is started'

     def stop(self):
         return f'{self.name} is stopped'

     def turn_right(self):
         return f'{self.name} is turned right'

     def turn_left(self):
         return f'{self.name} is turned left'

     def show_speed(self):
         return f'Current speed {self.name} is {self.speed}'


class TownCar(Car):
     def __init__(self, speed, color, name, is_police):
         super().__init__(speed, color, name, is_police)

     def show_speed(self):
         print(f'Current speed of town car {self.name} is {self.speed}')

         if self.speed > 40:
             return f'Speed of {self.name} is higher than allow for town car'
         else:
             return f'Speed of {self.name} is normal for town car'

class SportCar(Car):
     def __init__(self, speed, color, name, is_police):
         super().__init__(speed, color, name, is_police)


class WorkCar(Car):
     def __init__(self, speed, color, name, is_police):
         super().__init__(speed, color, name, is_police)

     def show_speed(self):
         print(f'Current speed of work car {self.name} is {self.speed}')

         if self.speed > 60:
             return f'Speed of {self.name} is higher than allow for work car'


class PoliceCar(Car):
     def __init__(self, speed, color, name, is_police):
         super().__init__(speed, color, name, is_police)

     def police(self):
         if self.is_police:
             return f'{self.name} is from police department'
         else:
             return f'{self.name} is not from police department'


bmw = SportCar(100, 'black', 'bmw', False)
smart = TownCar(20, 'white', 'smart', False)
mazda = WorkCar(40, 'green', 'mazda', True)
porsche = PoliceCar(110, 'yellow',  'porsche', True)
print(mazda.turn_left())
print(f'When {smart.turn_right()}, then {bmw.stop()}')
print(f'{mazda.go()} with speed exactly {mazda.show_speed()}')
print(f'{mazda.name} is {mazda.color}')
print(f'Is {bmw.name} a police car? {bmw.is_police}')
print(f'Is {mazda.name}  a police car? {mazda.is_police}')
print(bmw.show_speed())
print(smart.show_speed())
print(porsche.police())
print(porsche.show_speed())