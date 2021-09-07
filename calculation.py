def add(a, b=2):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b=2):
    return a * b


def divide(a, b):
    if b == 0:
        raise ValueError("Can not divide by zero")

    return a / b
