a = int(input("enter any number: "))
b = int(input("enter the number: "))
operater = input("enter the operation you want to perfrom: add , sub , mul , div:")

match operater:
    case "add":
        print("a + b =", a + b)
    case "sub":
        print("a - b =", a - b)
    case "div":
        if a == 0:
            print("invaid value can't enter zero in value1 for division")
        else:   
            print("a / b =", a / b)
    case "mul":
        print("a * b =", a * b)