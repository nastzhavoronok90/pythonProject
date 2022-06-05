#1 Создать программный файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
# Об окончании ввода данных будет свидетельствовать пустая строка.
f = open(r'data.txt', 'w', encoding='utf-8')
try:
    while True:
        name = input('Name: ')
        if name == '':
            break
        age = int(input('Age: '))
        car = input('Car yes/no: ')
        pets = input('Pets: ')
        print(name)
        print(age)
        print(car)
        print(pets)
        f.write(f'{name}, {age}, {car}, {pets}')
except ValueError:
    print('end!')
f.close()


#2 Создать текстовый файл (не программно),
# сохранить в нём несколько строк, выполнить подсчёт строк и слов в каждой строке.

f = open(r'data.txt', 'r', encoding='utf-8')
i = 0
for line in f:
    i += 1
    word_co = len(line.split())
    amount = len(line)
    print(line, end='')
    print(f'Количество слов в {i} строке: {word_co}')
    print(f'Количество символов в {i} строке: {amount}')
print(f'Общее количество строк: {i}')
f.close()

#3 . Создать текстовый файл (не программно).
# Построчно записать фамилии сотрудников и величину их окладов (не менее 10 строк).
# Определить, кто из сотрудников имеет оклад менее 20 тысяч, вывести фамилии этих сотрудников.
# Выполнить подсчёт средней величины дохода сотрудников.

f = open(r'data.txt', 'r', encoding='utf-8')
aver_sal = 0
i = 0
for line in f:
    text = line.split()
    aver_sal = aver_sal + int(text[1])
    i += 1
    if int(text[1]) > 20000:
        print(f'{text[0]} имеет зарплату больше 20000')
print(f'Средняя заработная плата: {aver_sal/i}')
f.close()


#4 Напишите программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.


my_interpreter = {
    'one':'один',
    'two':'два',
    'three':'три',
    'four':'четыре'
}
f = open(r'data1.txt', 'r')
f_obj = open(r'text.txt', 'a', encoding='utf-8')
for elem in f:
    el = elem.split()
    for key, value in my_interpreter.items():
        t = key
        r = value
        if el[0] == t:
            el[0] = r

    print(el)
    print(f'{el}\n', file=f_obj, end='')
f.close()
f_obj.close()


#5 Создать (программно) текстовый файл, записать в него программно набор чисел, разделённых пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить её на экран.

with open(r'data2.txt', 'w+', encoding='utf-8') as f:
    f.write((input('Num: ')))
    f.seek(0)
    num = f.readline().split()
    summa = 0
    for el in num:
        summa += int(el)
    print(summa)
print(f.closed)


#6 Сформировать (не программно) текстовый файл.
# В нём каждая строка должна описывать учебный предмет и наличие лекционных, практических и лабораторных занятий
# по предмету. Сюда должно входить и количество занятий.
# Необязательно, чтобы для каждого предмета были все типы занятий.
# Сформировать словарь, содержащий название предмета и общее количество занятий по нему. Вывести его на экран.


res = {}
with open(r'data2.txt', 'r', encoding='utf-8') as f:
    for line in f:
        text = line.split()
        # res.append(text[0])
        s = ''
        my_sum = 0
        for el in text:
            if el.isdigit():
                s += el
            elif s != '':
                my_sum += int(s)
                s = ''
        print(my_sum)
        res[text[0]] = my_sum
print(res)



#7 Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
# Если фирма получила убытки, в расчёт средней прибыли её не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями,
# а также словарь со средней прибылью.
# Если фирма получила убытки, также добавить её в словарь (со значением убытков).
# Итоговый список сохранить в виде json-объекта в соответствующий файл.

import json

firm_profit = {}
my_aver = {}
res = []
aver = 0
i = 0

with open(r'text.txt', 'r', encoding='utf-8') as f:
    with open('json_1.json', 'w', encoding='utf-8') as f_obj:
        for line in f:
            text = line.split()
            pr_f = int(text[2]) - int(text[3])
            if pr_f > 0:
                aver += pr_f
                i += 1
                firm_profit[text[0]] = pr_f
            elif pr_f < 0:
                pass
        my_aver['average_profit'] = aver / i
        res.append(firm_profit)
        res.append(my_aver)
        print(res)

        json.dump(res, f_obj)

