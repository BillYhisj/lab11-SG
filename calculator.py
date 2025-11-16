import math

def add(a, b): return a + b

def subtract(a, b): return a - b

def multiply(a, b): return a * b

def divide(a, b): # b / a
    if a == 0:
        raise ZeroDivisionError("You can not divide a number by zero")
    else:
        return b / a

def logarithm(a, b): #loga(b) use math library/raise ValueError
    if a < 0 or b < 0:
         raise ValueError("math domain error")
    else:
        return math.log(b,a)

def exponent(a, b): return a**b




