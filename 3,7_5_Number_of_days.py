"""
Количество дней 😉

Напишите программу, которая определяет количество дней в заданном месяце.

Формат входных данных
На вход программе подаются год и порядковый номер месяца (начиная с 1), разделенные пробелом.

Формат выходных данных
Программа должна вывести единственное число — количество дней в введенном месяце.
"""

import calendar

s = input().split()
year, month = int(s[0]), s[1]
d = {}
month_list = list(calendar.month_name)
for i in range(len(month_list)):
    d[month_list[i]] = i
days = calendar.monthrange(year, d[month])
print(days[1])

'''
year, month = input().split()
month = list(calendar.month_name).index(month)
print(calendar.monthrange(int(year), int(month))[1])
'''