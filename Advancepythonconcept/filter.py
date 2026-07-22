def is_greater_than_9(x):
    if x > 9:
        return True
    else:
        return False
    
a = [ 1,2,3,4,5,6,7,234,9 ,2345,2345,2345,3456] 

new = list(filter(is_greater_than_9, a))
print(new)