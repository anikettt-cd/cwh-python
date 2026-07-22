
def logger(func):
    def wrapper():
        print("function is being called")
        func()
    return wrapper


@logger
def say_hello():
    print("hello")

say_hello()