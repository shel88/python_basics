"""
5. Реализовать структуру «Рейтинг», представляющую собой не
возрастающий набор натуральных чисел
(каждый элемент ряда меньше или равен предыдущему).

У пользователя необходимо запрашивать новый элемент рейтинга.
Если в рейтинге существуют элементы с одинаковыми значениями,
то новый элемент с тем же значением должен разместиться после них.

Подсказка. Например, набор натуральных чисел: 7, 5, 3, 3, 2.
Пользователь ввел число 3. Результат: 7, 5, 3, 3, 3, 2.
Пользователь ввел число 8. Результат: 8, 7, 5, 3, 3, 2.
Пользователь ввел число 1. Результат: 7, 5, 3, 3, 2, 1.

Набор натуральных чисел можно задать непосредственно в коде,
например, my_list = [7, 5, 3, 3, 2].
"""
my_list = [7, 5, 3, 3, 2]
rait = int(input("Введите новый элемент рейтинга: "))
numb = 0
for i in my_list:
    if i < rait:
        my_list.insert(numb, rait)
        print(my_list)
        break
    else:
        numb += 1
        if numb == len(my_list):
            my_list.append(rait)
            print(f"Пользователь ввёл число {rait}. Результат: {my_list}")
            break
