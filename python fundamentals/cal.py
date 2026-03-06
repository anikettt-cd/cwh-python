value1 = int(input("ENTER THE FIRST VALUE: "))
value2 = int(input("ENTER THE SECOND VALUE: "))

operater = input("enter the operation you want to perfrom: add , sub , mul , div:")

if operater== "add":
     print("value1 + value2 = " ,value1 + value2)
elif operater == "sub":
    print("value1 - value2 = " ,value1 - value2 )
elif operater == "mul":
    print("value1 * value2 = ", value1 * value2)
elif operater == "div":
    if value1 == 0:
        print("invalid value can't enter zero in value1 for division")
    else:
        print("value1 / value2 = ", value1 / value2)
        
            
   
    

           
          
      
