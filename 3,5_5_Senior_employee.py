"""
Сотрудники организации 😄
Дан список сотрудников организации, в котором указаны их фамилии, имена и даты рождения. 
Напишите программу, которая определяет самого старшего сотрудника из данного списка.

Формат входных данных
На вход программе в первой строке подается натуральное число 
n — количество сотрудников, работающих в организации. В последующих n строках вводятся данные о каждом сотруднике: 
имя, фамилия и дата рождения, разделённые пробелом. Дата рождения указывается в формате DD.MM.YYYY.

Формат выходных данных
Программа должна определить самого старшего сотрудника и вывести его дату рождения, имя и фамилию, разделив пробелом. 
Если таких сотрудников несколько, программа должна вывести их дату рождения, а также их количество, разделив пробелом.
"""

from datetime import *

n = int(input())
pattern = "%d.%m.%Y"
pattern_dt = datetime.strftime
birth_dict = {}
for i in range(n):
    # разбивка на имя/фамилия/дата рождения
    f_name, l_name, birth = input().split(" ")
    # разбивка на дату и имя + фамилия
    dt_birth = datetime.strptime(birth, pattern)
    name = f"{f_name} {l_name}"
    # добавление в словарь
    if dt_birth in birth_dict:
        birth_dict[dt_birth].append(name)
    else:
        birth_dict[dt_birth] = [name]
oldest_date = min(birth_dict)
names = [name for name in birth_dict[oldest_date]]
# Вывод результата
if len(names) > 1:
    print(f"{pattern_dt(oldest_date, pattern)} {len(names)}")
else:
    print(f"{pattern_dt(oldest_date, pattern)} {names[0]}")
