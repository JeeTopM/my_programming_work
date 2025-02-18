"""
Даны две даты — левая и правая границы диапазона соответственно. 

Напишите программу, которая из этого диапазона, включая границы, выводит, 
начиная с даты, у которой сумма дня и месяца нечетная, 
каждую третью дату, только если она не понедельник и не четверг.
"""

from datetime import  timedelta, datetime

start, end = input(), input()
pattern = "%d.%m.%Y"
dt = datetime.strptime
dt_start, dt_end = dt(start, pattern), dt(end, pattern)

while dt_start <= dt_end:
    if (dt_start.day + dt_start.month) % 2 != 0:
        break
    dt_start += timedelta(days=1)

while dt_start <= dt_end:
    if dt_start.weekday() != 0 and dt_start.weekday() != 3:
        print(dt_start.strftime(pattern))
    dt_start += timedelta(days=3)
