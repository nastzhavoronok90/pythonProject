'''
1 Создать класс TrafficLight (светофор).
определить у него один атрибут color (цвет) и метод running (запуск);
атрибут реализовать как приватный;
в рамках метода реализовать переключение светофора в режимы: красный, жёлтый, зелёный;
продолжительность первого состояния (красный) составляет 7 секунд, второго (жёлтый) — 2 секунды,
третьего (зелёный) — на ваше усмотрение;
переключение между режимами должно осуществляться только в указанном порядке (красный, жёлтый, зелёный);
проверить работу примера, создав экземпляр и вызвав описанный метод.
Задачу можно усложнить, реализовав проверку порядка режимов.
При его нарушении выводить соответствующее сообщение и завершать скрипт.
'''

from time import sleep

class TrafficLight():
    __color = ['red', 'yellow', 'green']

    def running(self):
        i = 0
        while i < 3:
            print(f'Переключение светофора \n'
                  f'{TrafficLight.__color[i]}')
            if i == 0:
                sleep(7)
            elif i == 1:
                sleep(2)
            elif i == 2:
                sleep(5)
            i += 1


run1 = TrafficLight()
run1.running()

'''
2. Реализовать класс Road (дорога).
определить атрибуты: length (длина), width (ширина);
значения атрибутов должны передаваться при создании экземпляра класса;
атрибуты сделать защищёнными;
определить метод расчёта массы асфальта, необходимого для покрытия всей дороги;
использовать формулу: длина*ширина*масса асфальта для покрытия одного кв. метра дороги асфальтом, толщиной в 1 см*число см толщины полотна;
проверить работу метода.
'''

class Road():

    def __init__(self, length, width):
        self._length = length
        self._width = width

    def info(self):
        print(f' Длинна дороги: {self._length}; Ширина дороги: {self._width}')

    def mass(self):
        m = int(input('Введиде массу асфальта: '))
        t = int(input('Введите толщину полотна: '))
        rez = self._length * self._width * m * t
        print(f'Масса асфальта, необходимого для покрытия всей дороги: {rez} тонн')

mass1 = Road(20, 5000)
mass1.info()
mass1.mass()

'''
3. Реализовать базовый класс Worker (работник).
определить атрибуты: name, surname, position (должность), income (доход);
последний атрибут должен быть защищённым и ссылаться на словарь, содержащий элементы: оклад и премия, 
например, {"wage": wage, "bonus": bonus};
создать класс Position (должность) на базе класса Worker; 
в классе Position реализовать методы получения полного имени сотрудника (get_full_name) и дохода с 
учётом премии (get_total_income);
проверить работу примера на реальных данных: создать экземпляры класса Position, 
передать данные, проверить значения атрибутов, вызвать методы экземпляров.
'''
class Worker():
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'Wage': wage, 'Bonus': bonus}

class Position(Worker):

    def get_full_name(self):
        return self.name + ' ' + self.surname

    def get_total_income(self):
        gti = self._income.get('Wage') + self._income.get('Bonus')
        print(f'Доход {self.name} {self.surname} в должности {self.position} с учетом премии: {gti} рублей')

pos1 = Position('Leo', 'Pots', 'advokat', 10000, 500)
print(pos1.get_full_name())
pos1.get_total_income()

pos2 = Position('Kate', 'Moris', 'doctor', 7500, 1500)
print(pos2.get_full_name())
pos2.get_total_income()


'''
4. Реализуйте базовый класс Car.
у класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
 А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда);
опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля;
для классов TownCar и WorkCar переопределите метод show_speed. 
При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов. 
Выполните доступ к атрибутам, выведите результат. 
Вызовите методы и покажите результат.
'''
class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police
        print(f'{self.speed}, {self.color}, {self.name}, {self.is_police}')

    def go(self):
        return f'{self.name} поехала'

    def stop(self):
        return f'{self.name} остановилась'

    def turn_left(self):
        return f'{self.name} повернула налево'

    def turn_rigth(self):
        return f'{self.name} повернула направо'

    def show_speed(self):
        return f'{self.name} движется со скоростью {self.speed} км\ч'


class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Автомобиль {self.name} движется со скоростью {self.speed} км/ч')
        if self.speed > 60:
            print(f'Автомобиль {self.name} превысил скорость!')

class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Автомобиль {self.name} движется со скоростью {self.speed} км/ч')
        if self.speed > 40:
            print(f'Автомобиль {self.name} превысил скорость!')

class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def police(self):
        if self.is_police == True:
            print(f'{self.name} из полицейского депортамента')
        else:
            print(f'{self.name} не принадлежит полицейскому депортаменту')


audi = TownCar(100, 'green', 'Audi', True)
mazda = SportCar(60, 'red', 'Mazda', False)
pego = WorkCar(80, 'black', 'Peugeot', True)
reno = PoliceCar(50, 'white', 'Reno', False)
print(f'Список марок автомобилей: {audi.name}, {mazda.name}, {pego.name}, {reno.name}')
print(f'Машины выкрашены в цвета: {audi.color}, {mazda.color}, {pego.color}, {reno.color}')
print(f'Скорости,с которыми едут авто: {audi.speed}, {mazda.speed}, {pego.speed}, {reno.speed}')
audi.show_speed()
pego.show_speed()
print(f'{reno.show_speed()},a {mazda.turn_left()}')
print(f'{pego.stop()} у светофора, {audi.turn_rigth()}, а {reno.go()} дальше')
print(audi.is_police)
print(mazda.go())

'''
5. Реализовать класс Stationery (канцелярская принадлежность).
определить в нём атрибут title (название) и метод draw (отрисовка). Метод выводит сообщение «Запуск отрисовки»;
создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер);
в каждом классе реализовать переопределение метода draw. Для каждого класса метод должен выводить уникальное сообщение;
создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.
'''
class Stationery:
    def __init__(self, title, color):
        self.title = title
        self.color = color
        print(f'Инструмент: {self.color} {self.title}')


    def draw(self):
        print('Запуск отрисовки')


class Pen(Stationery):

    def __init__(self, title, color, ink):
        super().__init__(title, color)
        self.ink = ink

    def draw(self):
        print(f'Ваш инструмент {self.color} {self.title}. Запускаем отрисовку ручкой. Ручка {self.ink}')


class Pencil(Stationery):
    def __init__(self, title, color, lead):
        super().__init__(title, color)
        self.lead = lead

    def draw(self):
        print(f'Ваш инструмент {self.color} {self.title}. Запускаем отрисовку карандашом. {self.lead} карандаш очень крошится.')

class Handle(Stationery):
    def __init__(self, title, color, paint_mat):
        super().__init__(title, color)
        self.paint_mat = paint_mat

    def draw(self):
        print(f'Ваш инструмент {self.color} {self.title}. Запускаем отрисовку маркером. {self.title} {self.paint_mat} очень быстро сохнет')

pencil1 = Pencil('Карандаш', 'красный', 'угольный')
pen1 = Pen('Ручка', 'синяя', 'шариковая')
handle1 = Handle('Маркер', 'белый', 'перманентный')
pencil1.draw()
pen1.draw()
handle1.draw()
print(f'В моем пенале лежит {handle1.title} {handle1.color} и {pen1.title} {pen1.color}. А {pencil1.lead} {pencil1.title} потерялся')

pencil2 = Pencil('Карандаш', 'простой', 'графитовый')
pen2 = Pen('Ручка', 'голубая', 'гелевая')
handle2 = Handle('Маркер', 'розовый', 'акриловый')
pencil2.draw()
pen2.draw()
handle2.draw()

