"""
Отображение вводимой даты в разрезе недели.
Вводим дату, например 09.05.1945
Выводим, что это была среда
+ изучил календарь, добавил возможность вывести месяц и год
"""

import locale
from datetime import date, timedelta, datetime
import calendar

try:
    locale.setlocale(locale.LC_ALL, "ru_RU.UTF-8")
    d, m, y = [int(i) for i in input("Введите дату в формате дд,мм,гггг: ").split(".")]
    dt = date(y, m, d)

    print("\n" f"Введена дата: {datetime.strftime(dt, '%x')}")
    print(f"День недели: {datetime.strftime(dt, '%A')}")

    while dt.weekday() != 0:
        dt -= timedelta(days=1)

    print("\n" "Неделя, в которой есть данная дата: ")
    for i in range(7):
        print(datetime.strftime(dt, "%d %B %Y - %A"))
        dt += timedelta(days=1)

    def calendar_output(text, calendar_func, *args):
        while True:
            s = input(text).lower()
            if s in "y, n":
                if s == "y":
                    print("\n", calendar_func(*args))
                break
            else:
                print("Пожалуйста, введите 'y' или 'n'.")

    calendar_output("Нужен ли календарь на месяц? y/n: ", calendar.month, dt.year, dt.month)
    calendar_output("Нужен ли календарь на год? y/n: ", calendar.calendar, dt.year)
except Exception as e:
    print(f"Произошла ошибка: {e}")