import time
from register import *
print("Welcome to the RIVER BANK")
time.sleep(1)

while True:
    try:
        register = int(input("Select your choice\nEnter 1 for Signing Up\nEnter 2 for Logging In\nEnter 3 to exit\n : "))
        
        if(register == 1 or register == 2):
            if register == 1:
                SignUp()
            else:
                SignIn()
        else:
            print("Please enter the appropriate input : 1 or 2")
        
    except ValueError:
        print("Invalid Input")
        break
        