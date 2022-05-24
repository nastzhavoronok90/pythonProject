#1

res_list = [2, 'London', 115, True, None, 'Moris', 1.5]
print(res_list)
for el in res_list:
    print(type(el))
print('end')

#2

spis = input().split()
print(spis
for i in range(0, len(spis) - 1, 2):
    spis[i], spis[i+1] = spis[i+1], spis[i]
print(spis)


#3
#list

spring = [3, 4, 5]
summer = [6, 7, 8]
autumn = [9, 10, 11]
winter = [1, 2, 3]
month = int(input('Введите месяц от 1 до 12: '))
for el in spring:
    if month == el:
        print('spring')
for el in summer:
    if month == el:
        print('summer')
for el in autumn:
    if month == el:
        print('autumn')
for el in winter:
    if month == el:
        print('winter')


#dict
months = {'spring': [3, 4, 5], 'summer': [6, 7, 8], 'autumn': [9, 10, 11], 'winter': [1, 2, 3]}
month = int(input('Введите месяц от 1 до 12: '))
for el in months:
    if month in months[el]:
        print(el)


#4.
stroka = input().split()
print(stroka)
for i, el in enumerate(stroka):
   print(i+1, el[0:10])


#5

my_rating = [8, 8, 6, 4, 4, 2]
new_grade = int(input('Ваша новая оценка: '))
i = 0
for element in my_rating:
    if element > new_grade:
        i += 1

my_rating.insert(i, new_grade)
print(my_rating)










