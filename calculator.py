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

def div(a, b):
    if b == 0:
        raise ZeroDivisionError("Thief! (undefined -- cannot divide by zero!)")
    return a / b

def logarithm(a, b):
    if b <= 0 or b == 1 or a <= 0:
        raise ValueError("Invalid logarithmic base or argument.")
    return math.log(a, b)

def exp(a, b):
    pow(a, b)