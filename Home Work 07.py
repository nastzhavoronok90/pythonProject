'''
Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()),
который должен принимать данные (список списков) для формирования матрицы.
Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
Примеры матриц: 3 на 2, 3 на 3, 2 на 4.

31    32         3    5    32        3    5    8    3
37    43         2    4    6         8    3    7    1
51    86        -1   64   -8
Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов
класса Matrix (двух матриц). Результатом сложения должна быть новая матрица.
Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой матрицы
складываем с первым элементом первой строки второй матрицы и т.д.
'''

class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix


    def __str__(self):
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
                print(self.matrix[i][j], end=' ')
            print()


    def __add__(self, other):
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
                print(self.matrix[i][j] + other.matrix[i][j], end=' ')
            print()
matr1 = Matrix([[1, 2, 3],[4, 5, 6],[7, 8, 9]])
print(matr1.matrix)
matr1.__str__()

matr2 = Matrix([[1, 1, 1], [1, 1, 1], [1, 1, 1]])
print(matr2.matrix)
matr2.__str__()
matr1 + matr2
"""
2. Реализовать проект расчёта суммарного расхода ткани на производство одежды. 
Основная сущность (класс) этого проекта — одежда, которая может иметь определённое название. 
К типам одежды в этом проекте относятся пальто и костюм. 
У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма). 
Это могут быть обычные числа: V и H, соответственно.
Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5), 
для костюма (2*H + 0.3). Проверить работу этих методов на реальных данных.
Реализовать общий подсчет расхода ткани. 
Проверить на практике полученные на этом уроке знания: реализовать абстрактные классы 
для основных классов проекта, проверить на практике работу декоратора @property.
"""

from abc import abstractmethod

class Clothes:

    @abstractmethod
    def total_cloth(self):
        pass


class Jasket(Clothes):  # пальто

    def __init__(self, size):
        self.__size = size

    @property
    def size(self):
        return self.__size
    @size.setter
    def size(self, new):
        if new <= 0:
            self.__size = 6.5
        else:
            self.__size = new

    def total_cloth(self):
        return f'Расход ткани на пошив пальто: {self.__size / 6.5 + 0.5}'


class Garb(Clothes):  # костюм
    def __init__(self, growth):
        self.__growth = growth

    @property
    def growth(self):
        return self.__growth

    @growth.setter
    def growth(self, new):
        if new <= 0:
            self.__growth = 1
        else:
            self.__growth = new

    def total_cloth(self):
        return f'Расход ткани на пошив костюмa: {2 * self.__growth + 0.3}'


jas1 = Jasket(6.5)
print(jas1.total_cloth())
jas1.size = -1
print(jas1.size)
print(jas1.total_cloth())
garb1 = Garb(1)
print(garb1.total_cloth())
garb1.growth = 0
print(garb1.growth)
print(garb1.total_cloth())


"""
2.1 
"""
from abc import abstractmethod

class Clothes:

    def __init__(self, size, growth):
        self.size = size
        self.growth = growth

    @property
    def total(self):
        return f'Общий расход ткани на пошив пальто и костюма: {self.size / 6.5 + 0.5 + (2 * self.growth + 0.3)}'

    @abstractmethod
    def total_cloth(self):
        pass

class Jasket(Clothes):          #пальто

    def __init__(self, size, growth):
        super().__init__(size, growth)

    def total_cloth(self):
        return f'Расход ткани на пошив пальто: {self.size / 6.5 + 0.5}'

class Garb(Clothes):            #костюм
    def __init__(self, size, growth):
        super().__init__(size, growth)


    def total_cloth(self):
        return f'Расход ткани на пошив костюмa: {2 * self.growth + 0.3}'


jas1 = Jasket(13, 0)
print(jas1.total_cloth())
gar1 = Garb(0, 2)
print(gar1.total_cloth())
clo = Clothes(13, 2)
print(clo.total)

"""
Реализовать программу работы с органическими клетками, состоящими из ячеек. Необходимо создать класс Клетка. 
В его конструкторе инициализировать параметр, соответствующий количеству ячеек клетки (целое число). 
В классе должны быть реализованы методы перегрузки арифметических операторов:
сложение (__add__()), 
вычитание (__sub__()), 
умножение (__mul__()), 
деление (__truediv__()). 
Данные методы должны применяться только к клеткам и выполнять увеличение,
 уменьшение, умножение и целочисленное (с округлением до целого) деление клеток, соответственно.
"""

class Cell:

    def __init__(self, quantity):
        self.quantity = int(quantity)

    def __add__(self, other):
        return self.quantity + other.quantity

    def __sub__(self, other):
        if (self.quantity - other.quantity) > 0:
            print(self.quantity - other.quantity)
        else:
            print('Вычитание не возможно')

    def __mul__(self, other):
        return self.quantity * other.quantity

    def __truediv__(self, other):
        return round(self.quantity // other.quantity)

    def make_order(self, cell_num):
        self.cell_num = cell_num
        row = ''
        for i in range(int(self.quantity // self.cell_num)):
            row += str('*' * self.cell_num + '\n')
        row += str(self.quantity % self.cell_num * '*')
        return row


cell1 = Cell(40)
print(cell1.quantity)

cell2 = Cell(20)
print(cell2.quantity)

print(cell1 + cell2)
print(cell1 - cell2)
print(cell1 * cell2)
print(cell1 / cell2)
print(cell1.make_order(12))
print(cell2.make_order(10))