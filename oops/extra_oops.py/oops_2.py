class person:
    __name = "Hemanshii"
    
    def __hello(self):
        print("hello person!")
        
    def welcome(self):
        self.__hello()   
    
    
    
p1 = person()
    
print(p1.welcome())
