class Employee:
    def __init__(self , salary):
        self._salary = salary

    @property
    def salary(self):
        return self._salary   
    @salary.setter
    def salary(self , new_salary_amaount):
        if (new_salary_amaount < 0):
            print("hey please dont set the negative value for the salary")
        else:
            self._salary = new_salary_amaount
             
    
a = Employee(234567) 
a.salary = 123456
print(a.salary)   
  
