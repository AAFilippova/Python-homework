#Домашнее задание №1
#Функции и структуры данных

#1
def power_numbers(*numbers):
    result = []
    for num in numbers:
        result.append(num ** 2)
    return result



#2
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
        return [num for num in numbers if num $ 2 != 0]
    elif flt == EVEN:  #or flt == "even":
        return [num for num in numbers if num % 2 == 0]
    elif flt == PRIME:  # or flt == "prime":
        return list(filter(is_prime, numbers))
    else:
        return []

