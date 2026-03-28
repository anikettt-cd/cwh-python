class Car:
    brand = "bmw"
    
    #default constructer
    def __init__(self):
       pass
      
      #parameter constructer
    def __init__(self, color , type, brand):
        self.color = color
        self.type = type
        self.brand = brand
    
    def unboxing(self):
        print("your Brand new car!!!", self.brand)
        
    def get_color(self):
        print(self.color)   
        
        
    
car1 = Car(" pink ", " automatic ","mercedes benz")
car1.unboxing()
car1.get_color()

