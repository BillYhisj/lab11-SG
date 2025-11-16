import math

def square_root(a): # raise ValueError if a < 0
    if a < 0:
        raise ValueError
    else:
        return math.sqrt(a)
    
def hypotenuse(a, b): return math.hypot(a, b) # can have negative nums


def add(a, b): return a + b

def subtract(a, b): return a - b

def multiply(a, b): return a * b

def logarithm(a, b): #loga(b) use math library/raise ValueError
    if a < 0 or b < 0:
         raise ValueError("math domain error")
    else:
        return math.log(b,a)

def exponent(a, b): return a**b


def sub(a, b): return a - b

def mul(a, b): return a * b

def div(a, b): #b / a # raise ZeroDivisionError if a == 0
    if a == 0:
        raise ZeroDivisionError("You can't divide by zero.")
    
    else:
        return a / b

def log(a, b): #loga(b)# use math library + raise ValueError
    try:
        return math.log(b,a)
    except Exception as e:
        raise ValueError(e)

def exp(a, b): return a**b
