"""
Функция get_the_fastest_func()

Реализуйте функцию get_the_fastest_func(), которая принимает два аргумента в следующем порядке:

funcs — список произвольных функций
arg — произвольный объект
Функция get_the_fastest_func() должна возвращать функцию из списка funcs, которая затратила 
на вычисление значения при вызове с аргументом arg наименьшее количество времени.
"""

import time


def get_the_fastest_func(func, arg):
    data = {}
    for f in func:
        start = time.time()
        f(arg)
        end = time.time()
        res = end - start
        data[f] = res
    return min(data, key=data.get)
