# def decorators(func):
#     def wrapper():
#         print("junior school completed")
#         func()
#         print("collage completed")

#     return wrapper   



# @decorators
# def school():
#     print("secondary school completed")

# # f = decorators(school)
# # f()
# school()

# different way to run decorators

def repeat(n):
    def decorators(func):
        def wrapper(a):
           for i in range (n):
               func(a)
        return wrapper
    return decorators

@repeat(2)
def say_hello(a):
    (print(f"hello!!! {a}"))

say_hello("jagdish") 

@repeat(4)
def say1_hello(a):
    (print(f"heyy!!! {a}"))

say1_hello("Aniket")    





# def repeat(n):
#     def decorators(func):
#         def wrapper(a):
#            for i in range (n):
#                func(a)
#         return wrapper
#     return decorators


# def say_hello(a):
#     (print(f"hello!!! {a}"))

# repeat(7)(say_hello)("harry")



# def repeat(n):
#     def decorators(func):
#         def wrapper(a):
#            for i in range(n):
#                func(a)
#         return wrapper
#     return decorators

# def say_hello(a):
#     print(f"hello!!! {a}")

# our_decorator = repeat(7)
# say_hello_decorated = our_decorator(say_hello)
# say_hello_decorated("harry")