# def sum(a , b , c):
#     return a + b +c 

# print(sum(23,234,234))
# args will be the tuple of all values passes to the sum
def sum(*args):
    # args will be the tuple of all values passes to the sum

    total = 0 
    for item in args:
        total += item
    return total

print(sum(1,2,3,89
))
