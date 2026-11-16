# https://github.com/rrathinam203/lab11--RR---HR-
# Partner 1: Rahul Rathinam
# Partner 2: Holly Rockwell

import math

def square_root(a):
    if a < 0:
        raise ValueError("Cannot calculate square root of a negative number.")
    return math.sqrt(a)

def hypotenuse(a, b):
    return math.hypot(a, b)

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def mul(a, b):
    return a * b

def divide(a, b):
    if a == 0:
        raise ZeroDivisionError("Division by zero is not allowed.")
    return b / a

def logarithm(a, b):
    if a <= 0 or a == 1 or b <= 0:
        raise ValueError("Invalid logarithmic base or argument.")
    return math.log(b, a)

def exp(a, b):
    return a ** b