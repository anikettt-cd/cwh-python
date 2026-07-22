class Book:
    def __init__(self , title , auther):
        self.title = title
        self.auther = auther

    def __str__(self):
        return(f"{self.title} by {self.auther}")

    def __len__(self):
         return len(self.title)  
    


b1 = Book("python in 90 days" , "harry")    
print(b1)
print(len(b1))

b2 = Book("JAVA", "Aniket")
print(b2)
print(len(b2))





   