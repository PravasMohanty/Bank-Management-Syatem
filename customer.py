from database import *

class Customer:
    def __init__(self, pan, name, accnt_num, accnt_bal, paswd, age, sex, address):
        self.__pan = pan
        self.__name = name
        self.__accnt_num = accnt_num
        self.__accnt_bal = accnt_bal
        self.__paswd = paswd
        self.__age = age
        self.__sex = sex
        self.__address = address
                
    def create_user(self):  
        db_query(f"""INSERT INTO customers (pan, name, account_number, account_balance, password, age, sex, address, status) VALUES(
            '{self.__pan}', 
            '{self.__name}', 
            {self.__accnt_num}, 
            {self.__accnt_bal},
            '{self.__paswd}', 
            {self.__age}, 
            '{self.__sex}', 
            '{self.__address}', 
            1);
""")
        
    def User_details(self):
        print(f"""
              Name : {self.__name}
              Pan : {self.__pan}
              Account Number : {self.__accnt_num}
              Balance : {self.__accnt_bal}
              Age : {self.__age}
              Sex : {self.__sex}
              Address : {self.__address}
              """)
    

        mydb.commit()