"""
1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
В рамках класса реализовать два метода. Первый, с декоратором @classmethod.
Он должен извлекать число, месяц, год и преобразовывать их тип к типу «Число».
 Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
Проверить работу полученной структуры на реальных данных.
"""

class Data:

    def __init__(self, day, month, year):
        self.d = day
        self.m = month
        self.y = year

    def __str__(self):
        return f'Дата: {self.d} {self.m} {self.y}'

    @classmethod
    def set_data(cls, data):
        d, m, y = data.split('-')
        return cls(d, m, y)

    @staticmethod
    def valid(data):
        if int(data.d) > 31 and day < 1:
            return 'Некорректно указан день'
        if 1 < int(data.m) > 12:
            return 'Некорректно указан месяц'
        if 1999 > int(data.y) > 2022:
            return 'Заданный год не входит в диапазон'
        else:
            return 'Временные параменты заданы верно'



di = '10-11-1999'
data1 = Data.set_data(di)
print(data1.d, data1.m, data1.y)
print(Data.valid(data1))

di2 = '29-05-1998'
data2 = Data.set_data(di2)
print(data2.d, data2.m, data2.y)
print(Data.valid(data2))



"""
2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на ноль. 
Проверьте его работу на данных, вводимых пользователем. 
При вводе нуля в качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.
"""
class DivisionByZero:
    def __init__(self, numerator, denumerator):
        self.numer = numerator
        self.denumer = denumerator

    def rezult(self):
        try:
            rez = self.numer / self.denumer
        except ZeroDivisionError:
            print('Деление на 0 не возможно!')
        else:
            print(f'Ok! Результат деления: {rez}')
        finally:
            print('Работа завершена!')

num1 = DivisionByZero(10, 5)
num1.rezult()

num2 = DivisionByZero(5, 0)
num2.rezult()

'''
3. Создайте собственный класс-исключение, который должен проверять содержимое списка на наличие только чисел. 
Проверить работу исключения на реальном примере. Запрашивать у пользователя данные и заполнять список необходимо только числами. 
Класс-исключение должен контролировать типы данных элементов списка.

Примечание: длина списка не фиксирована. 
Элементы запрашиваются бесконечно, пока пользователь сам не остановит работу скрипта, введя, например, команду «stop». 
При этом скрипт завершается, сформированный список с числами выводится на экран.

'''

class MyError:
    def __init__(self, *args):
        self.my_list = []

    def input_num(self):
        while True:
            try:
                num = int(input('Вводите числа через Enter: '))
                self.my_list.append(num)
                print(f'Список чисел: {self.my_list}')


            except ValueError:
                print('Вы ввели не число!')
                yes_no = input('Хотите продолжить? Введите n\y: ')
                if yes_no == 'y' or yes_no == 'Y':
                    num = int(input('Вводите числа через Enter: '))
                    self.my_list.append(num)
                    print(f'Список чисел: {self.my_list}')
                else:
                    print(f'Итоговый список чисел: {self.my_list}')
                    break



int1 = MyError()
int1.input_num()

"""
4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. 
А также класс «Оргтехника», который будет базовым для классов-наследников. Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс). 
В базовом классе определите параметры, общие для приведённых типов.
 В классах-наследниках реализуйте параметры, уникальные для каждого типа оргтехники.
 
5. 5. Продолжить работу над первым заданием. 
Разработайте методы, которые отвечают за приём оргтехники на склад и передачу в определённое подразделение компании. 
Для хранения данных о наименовании и количестве единиц оргтехники, а также других данных, можно использовать любую подходящую структуру (например, словарь).

6. Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных. 
Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.
Подсказка: постарайтесь реализовать в проекте «Склад оргтехники» максимум возможностей, изученных на уроках по ООП.

"""
class Sklad:
    def __init__(self):
        self._dict = {}

    def add_to(self, equipment):
        """
        добавляем на склад позиции по названию группы
        """
        self._dict.setdefault(equipment.group_name(), []).append(equipment)

    def extract(self, name):
        '''
        извлекаем позици по названию группы.
        '''
        if self._dict[name]:
            self._dict.setdefault(name).pop(0)



class DepodEquimpent:
    def __init__(self, name, model, price, amount):
        self.name = name
        self.mod = model
        self.pr = price
        self.em = amount
        self.group = self.__class__.__name__

    def group_name(self):
        return f'{self.group}'

    def __repr__(self):
        return f'{self.name}, Модель: {self.mod}, Цена за ед.: {self.pr}, Патия в шт.: {self.em}'


class Printer(DepodEquimpent):
    def __init__(self, name, model, price, amount, color):
        super().__init__(name, model, price, amount)
        self.col = color

    def __repr__(self):
        return f'{self.name}, Модель: {self.mod}, Цена за ед.: {self.pr}, Патия в шт.: {self.em}, Цвет печати: {self.col}'

    def action(self):
        return 'Принтер производит печать информации и изобращений на бумагу'


class Scanner(DepodEquimpent):
    def __init__(self, name, model, price, amount,origsize):
        super().__init__(name, model, price, amount)
        self.orsz = origsize

    def __repr__(self):
        return f'{self.name}, Модель: {self.mod}, Цена за ед.: {self.pr}, Патия в шт.: {self.em}, Формат скан. оригинала: {self.orsz}'

    def action(self):
        return 'Сканер делает копии текста или изображений с бумажного носителя в цифровой выд.'


class Xerox(DepodEquimpent):
    def __init__(self, name, model, price, amount, fax):
        super().__init__(name, model, price, amount)
        self.fax = fax

    def __repr__(self):
        return f'{self.name}, Модель: {self.mod}, Цена за ед.: {self.pr}, Патия в шт.: {self.em}, Наличие факса: {self.fax}'

    def action(self):
        return 'Ксерокс делает копии текста или изображения на бумажный носитель. Есть возможность отправки документа по факсу'


sklad = Sklad()

printer = Printer('SONY', 'EG-154', 100, 126, 'black\white')
scaner = Scanner('Hp', 'php-3110', 1000, 100, 'A4')
xerox = Xerox('Philips', 'DRK-0115', 1111, 500, 'NO')

# добавляем созданные объекты на склад
sklad.add_to(printer)
sklad.add_to(scaner)
sklad.add_to(xerox)

# Печать функциональных возможностей каждого устройства
print(scaner.action())
print(printer.action())
print(xerox.action())

# выводим склад
print(sklad._dict)

# забираем с склада позицию и выводим оставшиеся на складе позиции
sklad.extract('Scanner')
print()
print(sklad._dict)


"""
7. Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число». 
Реализуйте перегрузку методов сложения и умножения комплексных чисел. Проверьте работу проекта. 
Для этого создаёте экземпляры класса (комплексные числа), выполните сложение и умножение созданных экземпляров. 
Проверьте корректность полученного результата.
"""
class ComplexNumber:

    def __init__(self, a, b):
        self.a = a
        self.b = b



    def __str__(self):
        if self.a == 0 and self.b == 0:
            return f'rez = {self.a} + {self.b}*i. Результат rez = {self.a} является действительным.'
        elif self.a == 0 and self.b != 0:
            return f'rez = {self.a} + {self.b}*i. Результат rez = {self.b}*i является чисто мнимым.'
        else:
            return f'rez = {self.a} + {self.b}*i. Результат имеет решение.'

    def __add__(self, other):
        return f'Результат сложения комплексных чисел: {self.a + other.a} + {self.b + other.b}*i'

    def __mul__(self, other):
        return f'Результат умножение комплексных чисел:{self.a * other.a - self.b * other.b} + {self.a * other.b + self.b * other.a}*i'

r = ComplexNumber(-15, 13)
print(r.__str__())
r1 = ComplexNumber(21, -3)
print(r1.__str__())
print(r + r1)
print(r * r1)






