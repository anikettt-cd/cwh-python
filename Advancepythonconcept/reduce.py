from functools  import reduce

numbers = [ 1,2,3,4,5,6,1234,234,234]

def sum (a, b):
    return a + b
c = reduce(sum, numbers)
print(c)