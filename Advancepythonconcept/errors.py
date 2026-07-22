# while True: 
#     try:
#      a = int(input("Enter the number 1: "))
#      b = int(input("Enter the number 2: "))

#      print(f"the sum is {a + b} ")
    
#     except ValueError:
#       print("please dont perform bad typecast")

#     except ZeroDivisionError:
#       print("hey dont divide by 0")   

#     except Exception as e:
#       print("some error occurred!" , e.add_note)
      
a = int(input("Enter number 1 : "))
b = int(input("Enternumber 2 : "))

if b == 0:
    raise ValueError("please don't divide by 0 ")

print(f"the division is {a / b}")