class Car:
    
    color = "black"
    
    @staticmethod
    def start():
        print("Car is starting")
        
    @staticmethod
    def stop():
        print("Car is stopping")
        
class ToyotaCar(Car):
    def __init__(self, brand):
        self.brand = brand 

class fortuner(ToyotaCar):
    def __init__(self , type):
        self.type = type
        
car1 = fortuner("petrol")
print(car1.start())