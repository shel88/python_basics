"""
6)	Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет и наличие лекционных, практических и лабораторных занятий по этому предмету и их количество. Важно, чтобы для каждого предмета не обязательно были все типы занятий. Сформировать словарь, содержащий название предмета и общее количество занятий по нему. Вывести словарь на экран.
Примеры строк файла: Информатика:   100(л)   50(пр)   20(лаб).
                                        Физика:   30(л)   —   10(лаб)
                                        Физкультура:   —   30(пр)   —
Пример словаря: {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}
"""

new_dict = {}
with open("file.txt", 'r', encoding='utf-8') as file:
        lines = file.readlines()
        for line in lines:
            info = line.replace('(', ' ').split()
            new_dict[info[0][:-1]] = sum(int(i) for i in info if i.isdigit())
print(new_dict)
