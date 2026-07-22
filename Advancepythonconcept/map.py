numbers = [1,3,4,56,78,9,0]

def square(x):
    return x * x

new = list(map(lambda x : x * x, numbers))
print(new)