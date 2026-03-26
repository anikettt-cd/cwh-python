# class : class is a blueprint or a template . eg from for a exam that contains namw , age , fathers name ,  mothers name etc.

#Object : Specific instance creadted from the template (class.) eg . form ehich contains the data of john doe.

class Employee:
    company = "hp"
    
    def get_salary(self): # self is the important here because self is a way to refercnce the object of the class which is being created
        return 34000
    
e1 = Employee() # an object of class employee is created here 
print(e1.get_salary())  # Employee e's get salary method is called 

e2 = Employee()
print(e2.get_salary())  
print(e2.company)