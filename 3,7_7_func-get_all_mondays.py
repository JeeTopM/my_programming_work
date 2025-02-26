"""
Функция get_all_mondays()

Реализуйте функцию get_all_mondays(), которая принимает один аргумент:

year — натуральное число
Функция должна возвращать отсортированный по возрастанию список всех дат (тип date) года year, выпадающих на понедельник.
"""

import calendar
from datetime import date


def get_all_mondays(year):
    days_in_month = []
    for m in range(1, 13):
        month_calendar = calendar.monthrange(year, m)
        days_in_month.append(month_calendar[1])

    mondays = []
    for m in range(1, 13):
        for d in range(1, days_in_month[m - 1] + 1):
            if calendar.weekday(year, m, d) == 0:
                mondays.append(date(year, m, d))
    return mondays


year = int(input())
for month_in_year in get_all_mondays(year):
    print(month_in_year)
