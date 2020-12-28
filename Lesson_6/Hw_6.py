# Первая задача. Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
# Атрибут реализовать как приватный. В рамках метода реализовать переключение светофора в режимы: красный, желтый, зеленый.
# Продолжительность первого состояния (красный) составляет 7 секунд, второго (желтый) — 2 секунды, третьего (зеленый) — на ваше усмотрение.
# Переключение между режимами должно осуществляться только в указанном порядке (красный, желтый, зеленый).
# Проверить работу примера, создав экземпляр и вызвав описанный метод. Задачу можно усложнить, реализовав проверку порядка режимов,
# и при его нарушении выводить соответствующее сообщение и завершать скрипт.

import time

class TrafficLight:
    __color = 'red'

    def running(self):
        print('Светофор работает')

        self.__color = 'Красный'
        print(f'Установлен цвет: {self.__color}')
        time.sleep(7)

        self.__color = 'Желтый'
        print(f'Установлен цвет: {self.__color}')
        time.sleep(2)

        self.__color = 'Зеленый'
        print(f'Установлен цвет: {self.__color}')
        time.sleep(5)

        while True:
            self.running()

traff_light = TrafficLight()
print(traff_light.running())

# Вторая задача. Реализовать класс Road (дорога), в котором определить атрибуты:
# length (длина), width (ширина). Значения данных атрибутов должны передаваться
# при создании экземпляра класса. Атрибуты сделать защищенными.
# Определить метод расчета массы асфальта, необходимого для покрытия всего
# дорожного полотна. Использовать формулу: длина*ширина*масса асфальта для покрытия одного кв метра дороги асфальтом,
# толщиной в 1 см*число см толщины полотна. Проверить работу метода.
# Например: 20м*5000м*25кг*5см = 12500 т

class Road:
    _length = None
    _width = None
    __asphalt = 25 #кг
    __depth = 0.05 #м

    def __init__(self, length, width):
        self._width = width
        self._length = length

    def calculate(self):
        return self._length * self._width * self.__asphalt * self.__depth

road = Road(length=4000, width=25)
print(road.calculate())

#Третья задача. Реализовать базовый класс Worker (работник), в котором определить атрибуты:
# name, surname, position (должность),
# income (доход). Последний атрибут должен быть защищенным и ссылаться на словарь,
# содержащий элементы: оклад и премия, например, {"wage": wage, "bonus": bonus}.
# Создать класс Position (должность) на базе класса Worker.
# В классе Position реализовать методы получения полного имени сотрудника (get_full_name)
# и дохода с учетом премии (get_total_income).
# Проверить работу примера на реальных данных (создать экземпляры класса Position,
# передать данные, проверить значения атрибутов, вызвать методы экземпляров).

class Worker:

    name = None
    surname = None
    position = None
    _income = {
        'wage': 'wage',
        'bonus': 'bonus'
    }

class Position(Worker):

    def __init__(self, name:str, surname:str, wage:float, bonus:float):
        self.name = name
        self.surname = surname
        self._income['wage'] = wage
        self._income['bonus'] = bonus

    def get_full_name(self):
        return self.name + self.surname

    def get_total_income(self):
        return self._income['wage'] + self._income['bonus']

position = Position(name="Ivan", surname="Ivanov", wage=12.33, bonus=12.33)

print(position.get_full_name())
print(position.get_total_income())

#Четвертая задача. Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
# А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).
# Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый класс метод show_speed,
# который должен показывать текущую скорость автомобиля. Для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
# Выполните вызов методов и также покажите результат.

class Car:

    speed: float
    color: str
    name: str
    is_police: bool

    def go(self):
        return print('Поехали')

    def stop(self):
        return print('Приехали')

    def turn(self, direction):
        return print(f'Направляемся {direction}')

    def show_speed(self):
        return self.speed

class PoliceCar(Car):
    is_police = True
    name = 'FORD'
    color = 'White and black'
    speed = 100.0

class TownCar(Car):
    is_police = False
    name = "Jiguli"
    color = "Rjavyi"
    speed = 80.0

    def show_speed(self):
        if self.speed > 60:
            return 'Превышение скорости!! ' + str(self.speed)
        return str(self.speed)

class WorkCar(Car):
    is_police = False
    name = 'Kamaz'
    color = 'Orange'
    speed = 80

    def show_speed(self):
        if self.speed > 40:
            return 'Превышение скорости!! ' + str(self.speed)
        return str(self.speed)

class SporCar(Car):
    is_police = False
    name = 'ferrari'
    color = 'Red'
    speed = 180.0

tc = TownCar()
pc = PoliceCar()
sc = SporCar()
wc = WorkCar()

print(tc.__dict__)
print(pc.__dict__)
print(wc.__dict__)
print(sc.__dict__)

pc.go()
print(wc.turn(direction='туда'))
sc.speed = 10000

print(tc.__dict__)
print(pc.__dict__)
print(wc.__dict__)
print(sc.__dict__)

#Пятая задача. Реализовать класс Stationery (канцелярская принадлежность).
# Определить в нем атрибут title (название) и метод draw (отрисовка).
# Метод выводит сообщение “Запуск отрисовки.” Создать три дочерних класса Pen (ручка),
# Pencil (карандаш), Handle (маркер). В каждом из классов реализовать переопределение метода draw.
# Для каждого из классов метод должен выводить уникальное сообщение.
# Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.

class Stationery:
    title: str

    def draw(self):
        return 'some basic stuff'

class Pen(Stationery):
    title = 'Pen'

    def draw(self):
        return self.title

class Pencil(Stationery):
    title = 'Pencil'

    def draw(self):
        return self.title

class Handle(Stationery):
    title = 'Handle'

    def draw(self):
        return self.title

p = Pen()
pc = Pencil()
h = Handle()
s = Stationery()

print(s.draw())
print(h.draw())
print(p.draw())
print(pc.draw())