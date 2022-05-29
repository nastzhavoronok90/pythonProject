#1 Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
# Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.

def my_devis(arg_1, arg_2):
    return arg_1 / arg_2
try:
    arg_1 = int(input('Введите первое число: '))
    arg_2 = int(input('Введите второе число: '))

    res = my_devis(arg_1, arg_2)
    print(f'Результат: {res}')

except ValueError:
    print('Only Numbers!')
except ZeroDivisionError:
    print('Division by zero is not allowed!')


#2 Выполнить функцию, которая принимает несколько параметров,
# описывающих данные пользователя: имя, фамилия, год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы.
# Осуществить вывод данных о пользователе одной строкой.

def my_direct (**kwargs):
    return kwargs
print(my_direct(name='Sam', surmame='Rutt', year=1975, email='samrutt@tt.com', t_phone=125486))
print(my_direct(name='Leo', surmame='Kapp', year=1917, email='kap1917@ttt.com', t_phone=5245635))

# 3 Реализовать функцию my_func(), которая принимает три позиционных аргумента
# и возвращает сумму наибольших двух аргументов.

def sum_max (one, two, three):
    max_1 = one
    max_2 = two
    if max_2 > max_1:
        max_1 = two
        max_2 = one
        if three > max_1:
            max_2 = max_1
            max_1 = three
        elif three > max_2:
            max_1 = two
            max_2 = three
    return max_1 + max_2
print('Результат сложения: {}'.format(sum_max(21, 8, 7)))
print('Результат сложения: {}'.format(sum_max(10, 82, 7)))
print('Результат сложения: {}'.format(sum_max(2, 8, 75)))

#4 Программа принимает действительное положительное число x и целое отрицательное число y.
# Выполните возведение числа x в степень y. Задание реализуйте в виде функции my_func(x, y).
# При решении задания нужно обойтись без встроенной функции возведения числа в степень.
 #Подсказка: попробуйте решить задачу двумя способами.

# Первый — возведение в степень с помощью оператора **.
def my_func(x, y):
    return (1 / x ** y)
try:
    x = int(input('Введите значение x:'))
    y = int(input('Введите значение y:'))
    result = my_func(x, y)
    print('Результат: {}'.format(result))
except ValueError:
    print('Only numbers!')
except ZeroDivisionError:
    print('Division by zero is not allowed!')

# Второй — более сложная реализация без оператора **, предусматривающая использование цикла.
def my_func():
    x = int(input('Ввод x:'))
    y = int(input('Ввод y:'))
    i = 0
    res = 1
    while i < y:
        res = res * (1 / x)
        i += 1
    return res
print(my_func())



#5 Программа запрашивает у пользователя строку чисел, разделённых пробелом.
# При нажатии Enter должна выводиться сумма чисел. Пользователь может продолжить ввод чисел, разделённых пробелом и снова нажать Enter.
# Сумма вновь введённых чисел будет добавляться к уже подсчитанной сумме.
#Но если вместо числа вводится специальный символ, выполнение программы завершается.
# Если специальный символ введён после нескольких чисел, то вначале нужно добавить сумму
# этих чисел к полученной ранее сумме и после этого завершить программу.

def my_func_s():
    res = 0
    while True:
        num = input('Введите числа через пробел: ').split()
        for el in num:
            if el == '*':
                print(res)
                return
            else:
                el1 = int(el)
                res = res + el1
        print(res)
print(my_func_s())

#6-7 В программу должна попадать строка из слов, разделённых пробелом.
# Каждое слово состоит из латинских букв в нижнем регистре.
# Нужно сделать вывод исходной строки, но каждое слово должно начинаться с заглавной буквы.
# Используйте написанную ранее функцию int_func().

def int_func():
    text = input('Text: ')
    if text.islower() == True:
        print(text.title())
    else:
        print('only small letters')
int_func()

