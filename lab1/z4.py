__author__ = 'pasha'

def fib(num):
    a, b =0, 1
    while b<num:
        yield b
        a, b = b, a+b


