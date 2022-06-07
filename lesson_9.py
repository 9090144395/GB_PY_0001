# 1. Создать класс TrafficLight (светофор).
# определить у него один атрибут color (цвет) и метод running (запуск);
# атрибут реализовать как приватный;

# в рамках метода реализовать переключение светофора в режимы: красный, жёлтый, зелёный;
# продолжительность первого состояния (красный) составляет 7 секунд,
# второго (жёлтый) — 2 секунды,
# третьего (зелёный) — на ваше усмотрение;
# переключение между режимами должно осуществляться только в указанном порядке (красный, жёлтый, зелёный);
# проверить работу примера, создав экземпляр и вызвав описанный метод.
# Задачу можно усложнить, реализовав проверку порядка режимов.
# При его нарушении выводить соответствующее сообщение и завершать скрипт.

print()
print('Задание 1')
print('________________________________________________________')
print()

import time


class TrafficLight:
    # атрибуты класса
    __color = "зеленый"

    # методы класса
    def running(self):
        self.__color = "красный"
        print(f"Включаем  - {self.__color}")
        time.sleep(7)
        self.__color = "жёлтый"
        print(f"Включаем  - {self.__color}")
        time.sleep(2)
        self.__color = "зелёный"
        print(f"Включаем  - {self.__color}")


put_the_button = TrafficLight()
put_the_button.running()

# 2. Реализовать класс Road (дорога).
# определить атрибуты: length (длина), width (ширина);
# значения атрибутов должны передаваться при создании экземпляра класса;
# атрибуты сделать защищёнными;

# определить метод расчёта массы асфальта, необходимого для покрытия всей дороги;
# использовать формулу: длина * ширина * масса асфальта для покрытия одного кв. метра дороги асфальтом,
# толщиной в 1 см * число см толщины полотна;
# проверить работу метода.
# Например: 20 м*5000 м*25 кг*5 см = 12500 т.

print()
print('Задание 2')
print('________________________________________________________')
print()


class Road:

    def __init__(self, length=0, width=0):
        # атрибуты класса
        self._length = length
        self._width = width

    # методы класса
    def running_calc(self, weight, thicknesses):
        result = self._length * self._width * weight * thicknesses

        print(f"Расчет массы асфальта - {result / 1000} т.")


put_the_button = Road(20, 5000)
put_the_button.running_calc(25, 5)

# 3. Реализовать базовый класс Worker (работник).
# определить атрибуты: name, surname, position (должность), income (доход);
# последний атрибут должен быть защищённым и ссылаться на словарь,
# содержащий элементы: оклад и премия, например, {"wage": wage, "bonus": bonus};

# создать класс Position (должность) на базе класса Worker;
# в классе Position реализовать методы получения полного имени сотрудника (get_full_name)
# и дохода с учётом премии (get_total_income);
# проверить работу примера на реальных данных:
# создать экземпляры класса Position, передать данные, проверить значения атрибутов, вызвать методы экземпляров.

print()
print('Задание 3')
print('________________________________________________________')
print()


class Worker:

    def __init__(self, name=None, surname=None, position=None, income_wage=0, income_bonus=0):
        # атрибуты класса
        self._name = name
        self._surname = surname
        self._position = position
        self._income = {"wage": income_wage, "bonus": income_bonus}


class Position(Worker):

    # методы класса
    def __init__(self, name=None, surname=None, position=None, income_wage=0, income_bonus=0):
        super().__init__(name, surname, position, income_wage, income_bonus)

    def get_full_name(self):
        result = str(self._name) + " " + str(self._surname) + " ( " + str(self._position) + " ) "
        print(result)

    def get_total_income(self):
        result = self._income["wage"] + self._income["bonus"]
        print(result)


men_1 = Position('Иван', 'Иванов', 'инженер', 50, 100)
men_1.get_full_name()
men_1.get_total_income()


# 4. Реализуйте базовый класс Car.
# у класса должны быть следующие атрибуты:
# speed, color, name, is_police(булево).
# А также методы: go, stop, turn(direction), которые должны сообщать,
# что машина поехала, остановилась, повернула (куда);
# опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
# добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля;

# для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
#
# Создайте экземпляры классов, передайте значения атрибутов.
# Выполните доступ к атрибутам, выведите результат. Вызовите методы и покажите результат.

print()
print('Задание 4')
print('________________________________________________________')
print()

class Car:

    def __init__(self, speed_default=0, color_default=None, name_default=None, is_police_default=False):
        # атрибуты класса
        self.speed = speed_default
        self.color = color_default
        self.name = name_default
        self.is_police = is_police_default

    def go(self):
        print('Машина поехала')

    def stop(self):
        print('Машина остановилась')

    def turn(self, direction):
        print(f'Машина повернула {direction}')

    def show_speed(self):
        print(f'Текущая скорость автомобиля - {self.speed}')


class TownCar(Car):

    def __init__(self, speed_default=0, color_default=None, name_default=None, is_police_default=False):
        # атрибуты класса из родительского класса
        super().__init__(speed_default, color_default, name_default, is_police_default=False)

    def show_speed(self):
        if self.speed > 60:
            print('Превышение скорости')
        else:
            print(f'Текущая скорость автомобиля - {self.speed}')


class SportCar(Car):

    def __init__(self, speed_default=0, color_default=None, name_default=None, is_police_default=False):
        # атрибуты класса из родительского класса
        super().__init__(speed_default, color_default, name_default, is_police_default=False)


class WorkCar(Car):

    def __init__(self, speed_default=0, color_default=None, name_default=None, is_police_default=False):
        # атрибуты класса из родительского класса
        super().__init__(speed_default, color_default, name_default, is_police_default=False)

    def show_speed(self):
        if self.speed > 40:
            print('Превышение скорости')
        else:
            print(f'Текущая скорость автомобиля - {self.speed}')


class PoliceCar(Car):

    def __init__(self, speed_default=0, color_default=None, name_default=None, is_police_default=False):
        # атрибуты класса из родительского класса
        super().__init__(speed_default, color_default, name_default, is_police_default=True)


car_1 = TownCar(90, 'red', 'corolla', True)
car_2 = SportCar(120, 'blue', 'ferrari', True)
car_3 = WorkCar(80, 'black', 'ford', True)
car_4 = PoliceCar(100, 'yellow', 'lada')

print('car_1.name :', car_1.name)
print('car_1.is_police :', car_1.is_police)
print('car_4.is_police :', car_4.is_police)

car_1.go()
car_1.show_speed()
car_2.show_speed()

# 5. Реализовать класс Stationery (канцелярская принадлежность).
# определить в нём атрибут title (название) и метод draw (отрисовка).
# Метод выводит сообщение «Запуск отрисовки»;

# создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер);

# в каждом классе реализовать переопределение метода draw.
# Для каждого класса метод должен выводить уникальное сообщение;

# создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.

print()
print('Задание 5')
print('________________________________________________________')
print()

class Stationery:

    def __init__(self, title_default=None):
        # атрибуты класса
        self.title = title_default

    def draw(self):
        print('Запуск отрисовки')

class Pen(Stationery):

    def __init__(self, title_default=None):
        # атрибуты класса в родительском классе
        super().__init__(title_default)

    def draw(self):
        print('Запуск отрисовки дочернего класса Pen')

class Pencil(Stationery):

    def __init__(self, title_default=None):
        # атрибуты класса в родительском классе
        super().__init__(title_default)

    def draw(self):
        print('Запуск отрисовки дочернего класса Pencil')

class Handle(Stationery):

    def __init__(self, title_default=None):
        # атрибуты класса в родительском классе
        super().__init__(title_default)

    def draw(self):
        print('Запуск отрисовки дочернего класса Handle')


object_1 = Stationery()
object_2 = Pen()
object_3 = Pencil()
object_4 = Handle()

object_1.draw()
object_2.draw()
object_3.draw()
object_4.draw()