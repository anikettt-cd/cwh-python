
class Employee:
    company = "hp"
    
    def __init__(self , salary , name , bond, company ):
       self.name = name # create an instance atributes to name and assign it with salary
       self.salary = salary
       self.bond = bond
       self.company = company
    
    def get_salary(self): 
        return self.salary
    
    def get_info(self):
        print(f"the name of the employee is {self.name}. Salary is {self.salary}. the bond is for {self.bond} years ")
    
    
e1 = Employee(34000, "john Doe", 4, "asus")
print(e1.company) # this will always print instance attributes whenever present
print(Employee.company) # this will always print the class attributes

#Object introspectes
# print(dir(e1))
    