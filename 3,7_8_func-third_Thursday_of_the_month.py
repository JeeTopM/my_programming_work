'''
ТЧМ

Во многих музеях существует один день месяца, когда посещение музея для всех лиц или 
отдельных категорий граждан происходит без взимания платы. Например, в Эрмитаже это третий четверг месяца.

Напишите программу, которая определяет даты бесплатных дней посещения Эрмитажа в заданном году.

Формат входных данных
На вход программе подается натуральное число, представляющее год.

Формат выходных данных
Программа должна определить все даты бесплатных дней посещения Эрмитажа в введенном году и вывести их. 
Даты должны быть расположены в порядке возрастания, каждая на отдельной строке, в формате DD.MM.YYYY.
'''
import calendar
from datetime import date, datetime


def get_all_mondays(year):
    days_in_month = []
    for m in range(1, 13):
        month_calendar = calendar.monthrange(year, m)
        days_in_month.append(month_calendar[1])

    mondays = []
    for m in range(1, 13):
        cht = 1
        for d in range(1, days_in_month[m - 1] + 1):
            if calendar.weekday(year, m, d) == 3:
                if cht == 3:
                    tcm = date(year, m, d)
                    mondays.append(datetime.strftime(tcm, '%d.%m.%Y'))
                cht += 1
        cht = 1
    return mondays


year = int(input())
for month_in_year in get_all_mondays(year):
    print(month_in_year)