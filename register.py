#Registering functions:
from database import * 
import random , time
from customer import *
from bank import *

def SignUp():
    pan_number = input("Enter your Pan Number : ")
    
    pan_chk = db_query(f"SELECT pan FROM customers where pan = '{pan_number}' ;")
    if pan_chk and len(pan_chk ) != 0:
        print("User already exists with the same PAN Number, Try again !")
    else:
        name = input("Enter your Name : ")
        paswd = input("Enter your password : ")
        age = int(input("Enter your Age : "))
        sex = input("Enter your gender(M/F/O) : ")
        addrs = input("Enter your Permanent Address : ")
        accnt_num = None
        while True:
            accnt_num = random.randint(10000000,99999999)
            acnt_chk = db_query(f"SELECT * FROM CUSTOMERS WHERE account_number = '{accnt_num}' ; ")
            if acnt_chk:
                continue
            else:
                break
        
        cust_obj = Customer(pan_number, name, accnt_num , 0 ,paswd, age, sex, addrs )
        cust_obj.create_user()
        bank_obj = Bank(pan_number,accnt_num)
        
    
def SignIn():
    pan_number = input("Enter your Pan Number : ")
    psswd = input("Enter your password : ")
    
    user_chk = db_query(f"SELECT pan FROM customers where pan = '{pan_number}' AND password = '{psswd}';")  
    if user_chk and len(user_chk) != 0:
        details = db_query(f"SELECT * FROM customers WHERE pan = '{pan_number}' ;")
        details = details[0]
        if details[-1]:
            # print(f"PAN : {details[0]}\nName : {details[1]}\nAccount Number : {details[6]}\nAge : {details[3]}\nSex : {details[4]}\nAddress : {details[5]}")
            print("Logged In Successfully")
            time.sleep(0.5)
            
            account_number = details[1]
            bankobj = Bank(pan_number,account_number)
            while True:
                action = int(input("""
                  Options :\n
                  1 : Deposit Money
                  2 : Cash Withdrawal
                  3 : Send Money 
                  4 : View User Details 
                  5 : View All transactions 
                  6 : Update User details
                  7 : Terminate Account
                  8 : Log Out\n : 
                  """))
                
                if action in (1,2,3,4,5,6,7,8):
                    if action == 1:
                        amount = int(input("Enter amount to deposit : "))
                        bankobj.deposit(amount)
                        
                    elif action == 2:
                        amount = int(input("Enter amount to withdraw : "))
                        bankobj.withdraw(amount)
                    
                    elif action == 3:
                        amount = int(input("Enter amount to send : "))
                        reciever = input("Enter PAN ID of the reciever : ")
                        bankobj.transfer(reciever,amount)
                        
                    elif action == 4:
                        details = db_query(f"SELECT * FROM customers WHERE pan = '{pan_number}' ;")
                        details = details[0]
                        print(f"""
                              PAN Number: {details[0]}
                              Name: {details[1]}
                              Account Number: {details[2]} 
                              Balance: {details[3]}
                              Age: {details[5]}
                              Gender: {details[6]}
                              Address: {details[7]}
                              """)
                        time.sleep(0.5)
                    
                    elif action == 6:
                        bankobj.update_details()
                    
                    elif action == 5:
                        bankobj.view_transac()
                        time.sleep(1)
                        
                    
                    elif action == 7:
                        bankobj.Terminate()
                        
                    elif action == 8:
                        break
                    time.sleep(0.5)
                else:
                    print("Invalid choice of Operation ; Please Try Again")
            
            
        else:
            print("Invalid User PAN or Password")
    else:
        print("Invalid User PAN or Password")

        