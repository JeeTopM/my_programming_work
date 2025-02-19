"""
Функция index_of_nearest()

Реализуйте функцию index_of_nearest(), которая принимает два аргумента в следующем порядке:
* numbers — список целых чисел 
* number — целое число
Функция должна находить в списке numbers ближайшее по значению число к числу number и возвращать его индекс. 
Если список numbers пуст, функция должна вернуть число -1.
"""


def index_of_nearest(nums, n):
    if nums:
        minimum = min(nums, key=lambda num: abs(num - n))
        return nums.index(minimum)
    return -1

# примеры:
'''
print(index_of_nearest([], 17))
print(index_of_nearest([7, 13, 3, 5, 18], 0))
print(index_of_nearest([9, 5, 3, 2, 11], 4))
print(index_of_nearest([7, 5, 4, 4, 3], 4))
'''