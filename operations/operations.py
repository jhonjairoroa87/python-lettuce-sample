# coding=utf-8


def factorial(number):
    number = int(number)
    if (number == 0) or (number == 1):
        return 1
    else:
        return number*factorial(number-1)


def summation(number):
    number = int(number)
    if number == 0:
        return 0
    else:
        return number+summation(number-1)
