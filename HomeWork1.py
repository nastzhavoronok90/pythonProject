#1

name = 'Меня зовут Leo'
print(name)
age = 32
print(age)

name2 = input('Введите ваше имя: ')
age2 = int(input('Сколько вам лет? '))
school = int(input('Сколько лет назад вы закончили школу? '))
print(name2)
print(age2)
print(school)


#2

time = int(input('Введите время в секундах: '))
print(time)

hour = time // 3600
print(hour)
minute = (time - (hour * 3600)) // 60
print(minute)
sek = time % 60
print(sek)
hms = 'Сейчас {} : {} : {} '.format (hour, minute, sek)
print(hms)

#3

num = int(input('Введите число: '))
sum = num + (num * 11) + (num * 111)
print(sum)
# еще был вариаент через склеивание,
# чтобы получилось например 101010, если человек ввел число больше 9,
# затем реобразовать в числовой тип и сложить по формуле

#4

nam = int(input('Введите число: '))
res = nam % 10 #сохраняем последнюю цифру
nam = nam // 10
while nam > 0:
    last = nam % 10  # сохраняем вторую цифру
    if last > res:
        res = last
    nam = nam // 10 #отделяем ее
print(res)

#5.

rev = int(input('Введите сумму выручки: '))
costs = int(input('Укажите затраты: '))

profit = rev - costs
print('Показатель прибыли равен {}'.format(profit))
if profit > 0:
    print('Фирма прибыльная')
    rentab = profit/rev
    print('Рентабельность ровна {} '.format(rentab))
    emp = int(input('введите количество сотрудников'))
    prof = int(profit/emp)
    print('Прибыль в расчете на одного сотрудника: {}'.format(prof))
else:
    print('Фирма в убытке(')

#6

dist = int(input('Дистанция в первый день пробежки: '))
route = int(input('Введите нужную дистанцию: '))
day = 0

while dist < route:
    dist = dist * 1.1
    day += 1
print('Спортсмен достигнет нужной дистанции в беге за {} дней тренировки'.format(day))
