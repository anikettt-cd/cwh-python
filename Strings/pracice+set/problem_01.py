# name = "Aniket saini"

# print(name[0])
# print(name[-1])
# print(len(name))

# a = "hello"
# b = "world"

# print (a + " " + b)
# n = 0
for i in range(1,4):
    if (i == 1):     
      print(" * " * (i+2))
    elif (i == 2):
        print(((" * " * (i + (-1)))+ "   " + (" * " * (i + (-1)) )))
    elif (i == 3):
        print(" * " * (i))
        break

n = 3
for i in range(n):
    if (i == 0 or i == n - 1):
        print( " * " * n)
    else:
        print(" * " + "   "  + " * ")
        
    
       



