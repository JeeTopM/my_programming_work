'''
Сотрудники организации 😄
Дан список сотрудников организации, в котором указаны их фамилии, имена и даты рождения. 
Напишите программу, которая определяет, в какую из дат родилось больше всего сотрудников.

Формат входных данных
На вход программе в первой строке подается натуральное число n — количество сотрудников, 
работающих в организации. В последующих n строках вводятся данные о каждом сотруднике: 
имя, фамилия и дата рождения, разделённые пробелом. Дата рождения указывается в формате DD.MM.YYYY.

Формат выходных данных
Программа должна вывести дату, в которую наибольшее количество сотрудников отмечает день рождения, в формате DD.MM.YYYY. 
Если таких дат несколько, программа должна вывести их все в порядке возрастания, каждую на отдельной строке, в том же формате.
'''
from datetime import *

n = int(input())
pattern = "%d.%m.%Y"
pattern_dt = datetime.strftime
data = {}
for _ in range(n):
    *name, birthday = input().split()
    birthday = datetime.strptime(birthday, pattern)
    if birthday in data:
        data[birthday] += 1
    else:
        data[birthday] = 1
max_days = max(data.values())
spis_days = list(filter(lambda x: data[x] == max_days, data))
for i in range(len(spis_days)):
    print(datetime.strftime(spis_days[i], pattern))