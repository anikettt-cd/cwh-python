a = [ 1,2 ,3, 4,5, 5,65 ,46 , 44 ]

def cube(x):
  return x*x*x*x
 
            
l1 = list(map(cube , a))
print(l1)

def evennumber(x):
  return x%2==0

l2 = list(filter(evennumber , a))
print(l2)
