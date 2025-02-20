"""
Функция get_biggest() 🌶️🌶️

Реализуйте функцию get_biggest(), которая принимает один аргумент:
numbers — список целых неотрицательных чисел
Функция должна возвращать наибольшее число, которое можно составить из чисел из списка numbers. 
Если список numbers пуст, функция должна вернуть число -1.
"""


def get_biggest(numbers):
    n = list(map(str, numbers))
    res = ""
    if len(n) < 1:
        return -1
    else:
        for num in sorted(n, key=lambda x: x * 10, reverse=True):
            res += num
        return int(res)


# Примеры:
print(get_biggest([1, 2, 3]))  # ответ: 321
print(get_biggest([61, 228, 9, 3, 11]))  # ответ: 961322811
print(get_biggest([7, 71, 72]))  # ответ: 77271
print(get_biggest([]))  # ответ: -1
# Еще примеры на True/False
print(get_biggest([7, 71, 72]) == 77271)
print(get_biggest([0, 0, 0, 0, 0, 0]) == 0)
print(get_biggest([]) == -1)
print(get_biggest([72, 7274]) == 727472)
print(get_biggest([62, 626]) == 62662)
print(get_biggest([953, 9534]) == 9539534)
print(get_biggest([262, 26]) == 26262)
'''
Код авторов курса:

def get_biggest(numbers):
    if not numbers:
        return -1
    
    li = [str(i) for i in numbers]
    lenght = len(li)
    
    for i in range(lenght):
        index = i
        for j in range(i + 1, lenght):
            if li[j] + li[index] > li[index] + li[j]:
                index = j
        li[i], li[index] = li[index], li[i]
    
    return int(''.join(li))
'''