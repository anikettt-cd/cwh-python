a = " hey my name is aniket, what is your name?"

sum = 0
vowels = ["a", "e", "i", "o", "u"]

for char in a:
    if(char in vowels):
        sum+=1

print(f" there are {sum} vowels in the string")

str1 = "madam"

if(str1 == str1[::-1]):
    print("the string is a palindrome")
else:
    print("the string is not palindrome")
   
    




 