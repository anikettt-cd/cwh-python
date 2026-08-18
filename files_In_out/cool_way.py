








# cardno = str(input("Enter the card no: "))

# lastdigit = cardno[-4:]
# hidden = (("x" * 4 + ' ') * 3)+ lastdigit
# print(hidden)

# import sys
# import tty
# import termios

# def getch():
#     fd = sys.stdin.fileno()
#     old = termios.tcgetattr(fd)
#     try:
#         tty.setraw(fd)
#         return sys.stdin.read(1)
#     finally:
#         termios.tcsetattr(fd, termios.TCSADRAIN, old)

# digits = ""
# print("Enter card number: ", end="", flush=True)

# while True:
#     ch = getch()

#     # Stop when Enter is pressed
#     if ch == "\r" or ch == "\n":
#         break

#     # Ignore anything except digits
#     if not ch.isdigit():
#         continue

#     # Limit to 16 digits
#     if len(digits) == 16:
#         continue

#     # Print a space after every 4 digits
#     if len(digits) and len(digits) % 4 == 0:
#         print(" ", end="", flush=True)

#     print(ch, end="", flush=True)
#     digits += ch

# print("\n")

# if len(digits) == 16:
#     print("Original Card Number :", " ".join(digits[i:i+4] for i in range(0, 16, 4)))
#     print("Masked Card Number   :", "xxxx xxxx xxxx " + digits[-4:])
# else:
#     print("Please enter exactly 16 digits.")

with open("harry.txt", "r") as f :  #context manager
    content = f.read()
    print(content)
    
    #no need  to write f.close() because file is already closed by default when usinf with syntex and with is a context manager 

  
