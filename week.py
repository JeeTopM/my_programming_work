"""
Отображение вводимой даты в разрезе недели.
Вводим дату, например 09.05.1945
Выводим, что это была среда + всю неделю этой даты
"""

import locale
from datetime import date, timedelta, datetime

locale.setlocale(locale.LC_TIME, "ru_RU.UTF-8")
d, m, y = [int(i) for i in input("Введите дату в формате дд,мм,гггг: ").split(".")]
dt = date(y, m, d)

print("\n" f"Введена дата: {datetime.strftime(dt, '%x')}")
print(f"День недели: {datetime.strftime(dt, '%A')}")
print("\n" "Неделя, в которой есть данная дата: ")

while dt.weekday() != 0:
    dt -= timedelta(days=1)

for i in range(7):
    print(datetime.strftime(dt, "%d %B %Y - %A"))
    dt += timedelta(days=1)
    if dt.weekday() == 0:
        break
