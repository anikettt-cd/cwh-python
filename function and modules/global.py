z = 15

def fun(a , b):
    print("hey we are doing sum here ")
    c = a + b
    global z
    z = 0
    return c


print(fun ( 5,123))
print(z)
