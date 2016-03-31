# coding=utf-8
from lettuce import world, step
from operations.operations import factorial, summation


@step('I have the number (\d+)')
def have_the_number(step, number):
    world.number = int(number)


@step('I compute its factorial')
def compute_its_factorial(step):
    world.number = factorial(world.number)


@step('I compute its summation')
def compute_its_factorial(step):
    world.number = summation(world.number)


@step('I see the number (\d+)')
def check_number(step, expected):
    expected = int(expected)
    assert world.number == expected, \
        "Got %d" % world.number


