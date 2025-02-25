"""
День недели

Напишите программу, которая определяет день недели, соответствующий заданной дате.

Формат входных данных
На вход программе подается дата в формате YYYY-MM-DD.

Формат выходных данных
Программа должна вывести полное название дня недели на английском, который соответствует введенной дате.
"""

import calendar
from datetime import datetime
import time

s = input()

# daterime
start = time.time()
dt = datetime.strptime(s, "%Y-%m-%d")
print(datetime.strftime(dt, "%A"))
end = time.time()
print(end - start)

# calendar 1
start = time.time()
y, m, d = map(int, s.split("-"))
print(calendar.day_name[calendar.weekday(y, m, d)])
end = time.time()
print(end - start)

# calendar 2
start = time.time()
dt = datetime.fromisoformat(s)
print(list(calendar.day_name)[dt.weekday()])
end = time.time()
print(end - start)
