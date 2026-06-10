class Employee:
    def __init__(self , name ,salary ):
        self.name = name 
        self.salary = salary

    @property   
    def first_name(self):
        f = self.name.split(" ") 
        return f[0]   
    
    @first_name.setter
    def first_name(self , first):
        f = self.name.split(" ")
        new_name = f"{first} {f[1]}"
        self.name = new_name


e = Employee("Jack doe", 3635243)

print(e.first_name) 
e.first_name = "john"
print(e.name)          
