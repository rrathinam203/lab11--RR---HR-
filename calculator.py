import math

def add(a, b): 
    return a + b

def sub(a, b): 
    return a - b

def mul(a, b): 
    return a * b

def div(a, b):
    if a == 0:
        raise ZeroDivisionError("Thief! (undefined -- cannot divide by zero!)")
    return b / a

def log(a, b):
    if a <= 0:
        raise ValueError("Thief! (undefined -- base must be greater than zero!)")
    return math.log(b, a)

def exp(a, b):
    pow(a, b)

