def prime_numbers(n):
    
    if n <=1:
        return False
      
    for i in range(2 , n):
        if n % i == 0:
            return False
        
    return True



def sepreate_primes(n):
 not_prime = []
 prime = []
 
 for num in range( 2 , n+1):
     if prime_numbers(num):
         prime.append(num)
     else:
         not_prime.append(num)

 return  f"this are the prime numbers until {n}:{prime} \n this the numbers which are not prime until {n} : {not_prime}"         




def createfile(prime_text):
    
 with open("prime.txt", "a") as f:
      f.write(prime_text)
   
 return   "success"

prime_text = sepreate_primes(100)
print(prime_text)

print(createfile(prime_text))
              
         
          
          
          
          
            










   
  
        