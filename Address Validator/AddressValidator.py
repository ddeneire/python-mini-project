import re 
def addressVal(address):
    pattern = r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$"
    if re.match(pattern, address):
        print("Valid email")
    else:
        print("Invalid email")

print("This program will decide if your input is a valid email address")
while(True):
    print("A valid email address needs an '@' symbol and a '.'")
    x = input("Input your email address:")

    addressVal(x)
