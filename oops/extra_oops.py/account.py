class Account:
    def __init__(self , bal , acc):
        self.balance = bal
        self.account = acc
        
    def debit(self, amount):
        self.balance -= amount
        print("Rs", amount , "debited from your account")
        print(self.get_balance() , "your current balance is: " )
        
    def credit(self , amount):
        self.balance += amount
        print("Rs" , amount , "credited to your account")
        print(self.get_balance() , "your current balance is: " )
     
    def get_balance(self):
        return self.balance    
            
            
        
acc1 = Account(10000, 123456789)
print("your account balance is: " , acc1.balance)
print("your account number is: " , acc1.account)

acc1.debit(2000)        

acc1.credit(4000)


      