class Mathutils:
    def __init__(self):
        pass

    @staticmethod
    def add(a ,b):
        return (a + b)
    
    @classmethod
    def description(cls):
        print("this is the utility classs for the math operrtaion")
# a = Mathutils
# print(a.add(123,123))
# a.description()

Mathutils.description()
print(Mathutils.add(23,34))

