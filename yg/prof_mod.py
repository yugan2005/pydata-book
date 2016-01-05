from numpy.random import randn

def add_and_sum(x, y):
    added = x+y
    summed = added.sum(axis=1)
    return summed

def call_function():
    x = rand(1000, 1000)
    y = rand(1000, 1000)
    return add_and_sum(x, y)
