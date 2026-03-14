def sum(a , b):
    c =  a + b
    z = 1
    return c


def greet():
    z = 32 #  here z is local variable
    print("hello")

z = 8 # z is global variable 
print(z)

print(sum(2,3))
print(z)