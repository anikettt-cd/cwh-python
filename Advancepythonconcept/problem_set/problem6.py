class NegativeNumberError(Exception):
     pass

try:
    num = int(input("Enter the number:"))

    if num < 0:
          raise NegativeNumberError(" Number cannot be negative")
    
    result = 45/num
    print(f"the result is {result}")


except ValueError:
     print("Error: please enter the proper number") 

except ZeroDivisionError:
     print("Error: cannot be divide by zero")  

except NegativeNumberError as e:
     print(f"Error: {e} " )           


    
     

     
