#"""
#Домашнее задание №1
#Функции и структуры данных
#"""


def power_numbers(*numbers):
    result = []
    for num in numbers:
        result.append(num ** 2)
    return result


#   """
#    функция, которая принимает N целых чисел,
#    и возвращает список квадратов этих чисел
#    >>> power_numbers(1, 2, 5, 7)
#    <<< [1, 4, 25, 49]
#    """


import math

ODD = "odd"
EVEN = "even"
PRIME = "prime"


def is_prime(num):
    if num < 2:
        return False
    for n in range(2, int(math.sqrt(num) + 1)):
        if num % n == 0:
            return False
    return True


def filter_numbers(numbers, flt):
    if flt == ODD:  # or flt == "odd":
        return [num for num in numbers if num % 2 != 0]
    elif flt == EVEN:  #or flt == "even":
        return [num for num in numbers if num % 2 == 0]
    elif flt == PRIME:  # or flt == "prime":
        return list(filter(is_prime, numbers))
    else:
        return []

#   """
#   функция, которая на вход принимает список из целых чисел,
#    и возвращает только чётные/нечётные/простые числа
#   (выбор производится передачей дополнительного аргумента)
#
#   >>> filter_numbers([1, 2, 3], ODD)
#   <<< [1, 3]
#    >>> filter_numbers([2, 3, 4, 5], EVEN)
#    <<< [2, 4]
#    """
