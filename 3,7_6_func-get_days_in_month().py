"""
Функция get_days_in_month()   

Реализуйте функцию get_days_in_month(), которая принимает два аргумента в следующем порядке:

year — натуральное число
month — полное название месяца на английском
Функция должна возвращать отсортированный по возрастанию список всех дат (тип date) месяца month и года year.
"""

import calendar
from datetime import timedelta, date


def get_days_in_month(year, month):
    list_month = list(calendar.month_name)
    data_month = {}
    for i in range(len(list_month)):
        data_month[list_month[i]] = i
    days = calendar.monthrange(year, data_month[month])
    days_in_month = days[1]
    start_day = date(year, data_month[month], 1)
    all_days = []
    for i in range(days_in_month):
        all_days.append(start_day)
        start_day += timedelta(days=1)
    return all_days


# Авторы
"""
def get_days_in_month(year, month):
    month = list(calendar.month_name).index(month)
    return [date(year, month, day) for day in range(1, calendar.monthrange(year, month)[1] + 1)]
"""

# Тест
print(get_days_in_month(2021, "December"))
year, month = input().split()
print(get_days_in_month(int(year), month))
