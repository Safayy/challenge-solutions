import numpy

def find_difference(a, b):
    a_total = b_total = 1
    for i in range(len(a)):
        a_total *= a[i]
        b_total *= b[i]
    return a_total - b_total if a_total - b_total>=0 else b_total - a_total

def find_difference(a, b):
    return abs(numpy.prod(a) - numpy.prod(b))
    
print( find_difference([2, 2, 3], [5, 4, 1]) )