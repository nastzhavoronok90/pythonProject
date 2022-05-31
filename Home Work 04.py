#1 Реализовать скрипт, в котором должна быть предусмотрена функция расчёта заработной платы сотрудника.
# Используйте в нём формулу: (выработка в часах*ставка в час) + премия.
# Во время выполнения расчёта для конкретных значений необходимо запускать скрипт с параметрами.

from sys import argv

prod, bid, bonus = map(int, argv[1:])
print('Выработка в часах: {}'.format(prod))
print('Ставка в час: {}'.format(bid))
print('Премия: {}'.format(bonus))
salary = (prod * bid) + bonus
print('Заработная плата состаляет: {}'.format(salary))

#2 Представлен список чисел.
# Необходимо вывести элементы исходного списка, значения которых больше предыдущего элемента.

try:
    spis = list(map(int,input('Num: ').split()))
    new_spis = [spis[i+1] for i in range(len(spis) - 1) if spis[i+1] > spis[i]]
    print(new_spis)
except ValueError:
    print('Only numbers!')

#3 Для чисел в пределах от 20 до 240 найти числа, кратные 20 или 21. Решите задание в одну строку.

new_sp = [el for el in range(20, 240) if el % 20 == 0 or el % 21 == 0]
print(new_sp)

#4 Представлен список чисел. Определите элементы списка, не имеющие повторений.
# Сформируйте итоговый массив чисел, соответствующих требованию.
# Элементы выведите в порядке их следования в исходном списке.
# Для выполнения задания обязательно используйте генератор.

try:
    spisok = list(map(int,input('Num: ').split()))
    n_spis = [el for el in spisok if spisok.count(el) == 1]
    print(n_spis)
except ValueError:
    print('Only numbers!')

#5 Реализовать формирование списка, используя функцию range() и возможности генератора.
# В список должны войти чётные числа от 100 до 1000 (включая границы).
# Нужно получить результат вычисления произведения всех элементов списка.

from functools import reduce
def gener(a, b):
    return a * b
spis_n = [el for el in range(100, 1001) if el % 2 == 0]
print(reduce(gener, spis_n))

#6 Реализовать два небольших скрипта:
#1) итератор, генерирующий целые числа, начиная с указанного;
#2) итератор, повторяющий элементы некоторого списка, определённого заранее.

from itertools import count, cycle
#1)
try:
    num = int(input('Number < 40: '))
    for el in count(num, 2):
        print(el)
        if el == 50:
            break
except ValueError:
    print('Only numbers!')

#2)
name = input('Напишите ваше имя: ').split()
i = 0
for elem in cycle(name):
    print(elem)
    i += 1
    if i == 5:
        break


#7 Реализовать генератор с помощью функции с ключевым словом yield, создающим очередное значение.
# При вызове функции должен создаваться объект-генератор.
# Функция вызывается следующим образом: for el in fact(n). Она отвечает за получение факториала числа.
# В цикле нужно выводить только первые n чисел, начиная с 1! и до n!.

from math import factorial
try:
    def func_n():
        for i in range(1,int(input('Num:'))):
            yield i
    print(func_n())
    for el in func_n():
        el = factorial(el)
        print(el)
except ValueError:
    print('Only numbers!')