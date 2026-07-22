from functools import reduce
l = [1,2,3,4]

def product(a , b):
    return a * b

print(reduce(product , l))