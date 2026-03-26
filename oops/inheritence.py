class Animal: # parent class
    location = "Earth"
    def __init__(self,name):
        self.name = name
    def speak(self):
        print("Speaking now........ ") 
        
class Dog(Animal): # this is now inheritance is done in python
    def speak(self):
        super().speak()  # we are using the speaking functionn of the parent class.
        print("woofff!")            
        
a = Dog("Bruno")
a.speak() 
print(a.location)       