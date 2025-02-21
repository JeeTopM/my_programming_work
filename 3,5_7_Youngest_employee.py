"""
Сотрудники организации 😔

Дан список сотрудников организации, в котором указаны их фамилии, имена и даты рождения. 
Напишите программу, которая определяет самого молодого сотрудника, празднующего свой 
день рождения в течение ближайших семи дней от текущей даты.

Формат входных данных
На вход программе в первой строке подается текущая дата в формате DD.MM.YYYY, 
в следующей строке вводится натуральное число n — количество сотрудников, работающих в организации. 
В последующих n строках вводятся данные о каждом сотруднике: имя, фамилия и дата рождения, разделённые пробелом. 
Дата рождения указывается в формате DD.MM.YYYY.

Формат выходных данных
Программа должна определить самого молодого сотрудника, празднующего свой день рождения в течение ближайших семи дней,
и вывести его имя и фамилию, разделив пробелом. Если таких сотрудников нет, программа должна вывести текст: 
Дни рождения не планируются
"""

from datetime import datetime, timedelta

pattern = "%d.%m.%Y"
data_now = datetime.strptime(input(), pattern)
data_sev = data_now + timedelta(days=7)
candidates = {}


for _ in range(int(input())):
    *name, birth = input().split(" ")
    birthday = datetime.strptime(birth, pattern)
    name = " ".join(name)
    days = 0
    if data_now < birthday.replace(year=data_now.year) <= data_sev:
        days = (birthday.replace(year=data_now.year) - data_now).days
    elif data_now < birthday.replace(year=data_sev.year) <= data_sev:
        days = (birthday.replace(year=data_sev.year) - data_now).days
    else:
        continue
    candidates["".join(name)] = birthday.year

if len(candidates) == 0:
    print("Дни рождения не планируются")
else:
    max_key = max(candidates, key=candidates.get)
    print(max_key)
