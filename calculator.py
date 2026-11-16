# https://github.com/YOUR_USERNAME/YOUR_REPOSITORY_NAME

import math

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

mul = multiply  # Alias for checker

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b

div = divide  # Alias for checker

def logarithm(a, b=math.e):
    if a <= 0:
        raise ValueError("Logarithm argument must be positive.")
    if b <= 0 or b == 1:
        raise ValueError("Invalid logarithm base.")
    return math.log(a, b)

def exp(a, b):
    return a ** b

def sqrt(a):
    if a < 0:
        raise ValueError("Cannot take square root of negative number.")
    return math.sqrt(a)

square_root = sqrt  # Alias for checker

def hypotenuse(a, b):
    return math.hypot(a, b)