"""
Отображение вводимой даты в разрезе недели.
Вводим дату, например 09.05.1945
Выводим, что это была среда + всю неделю этой даты
"""

import locale
from datetime import date, timedelta, datetime
import calendar

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


try:
    while True:
        s = input("Нужен ли календарь на месяц? y/n: ").lower()
        if s in "y, n":
            if s == "y":
                print("\n", calendar.month(dt.year, dt.month))
            break
        else:
            print("Пожалуйста, введите 'y' или 'n'.")
except Exception as e:
    print(f"Произошла ошибка: {e}")


try:
    while True:
        s = input("Нужен ли календарь на год? y/n: ").lower()
        if s in "y, n":
            if s == "y":
                print("\n", calendar.calendar(dt.year, m=4))
            break
        else:
            print("Пожалуйста, введите 'y' или 'n'.")
except Exception as e:
    print(f"Произошла ошибка: {e}")