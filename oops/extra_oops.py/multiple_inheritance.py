class A :
    varA = "I am variable A"

class B :
    varB = "I am variable B"

class C(A, B) :
    varC = "I am variable C"
    
c1 = C() 
print(c1.varA)   
print(c1.varB)   
print(c1.varC)   