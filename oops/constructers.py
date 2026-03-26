
class Employee:
    
    def __init__(self , salary , name , bond):
       self.name = name # create an instance atributes to name and assign it with salary
       self.salary = salary
       self.bond = bond
    
    def get_salary(self): 
        return self.salary
    
    def get_info(self):
        print(f"the name of the employee is {self.name}. Salary is {self.salary}. the bond is for {self.bond} years ")
    
    
e1 = Employee(34000, "john Doe", 4)
e1.get_info()
    
    