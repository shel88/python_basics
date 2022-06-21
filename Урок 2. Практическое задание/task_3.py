"""
3. Пользователь вводит месяц в виде целого числа от 1 до 12.
Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
Напишите два варианта решения: через list и через dict.

Пример:
Введите номер месяца: 10
Результат через список: Осень
Результат через словарь: Осень
"""
dict1 = {'Зима': (12, 1, 2), 'Весна': (3, 4, 5), 'Лето': (6, 7, 8), 'Осень': (9, 10, 11)}
list1 = [12, 1, 2]
list2 = [3, 4, 5]
list3 = [6, 7, 8]
list4 = [9, 10, 11]

month = int(input('Введите номер месяца: '))
for key in dict1.keys():
    if month in dict1[key]:
        print(f"Результат через словарь: {key}")

if month in list1:
    print('Результат через список: Зима')
if month in list2:
    print('Результат через список: Весна')
if month in list3:
    print('Результат через список: Лето')
if month in list4:
    print('Результат через список: Осень')
