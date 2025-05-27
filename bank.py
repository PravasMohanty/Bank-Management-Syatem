from database import *
import datetime

def getTime():
    return datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

class Bank:
    def __init__(self , pan_number , account_number):
        self.__pan_number = pan_number
        self.__account_number = account_number
        self.create_transaction_table()
        
    def create_transaction_table(self):
            db_query(f"""
                     CREATE TABLE IF NOT EXISTS {self.__pan_number}_transactions (
                     transaction_time TIME,
                     transaction_type VARCHAR(10),
                     counterparty_account VARCHAR(20),
                     post_transaction_balance INTEGER
                     );
                     """)
            
    def deposit(self, amount):
        
        last_transac = db_query(f"""
                                SELECT account_balance FROM customers
                                WHERE pan = '{self.__pan_number}';
                                """)
        current_time = getTime()
        balance = 0
        if last_transac:
            balance = last_transac[0][0]
        
        db_query(f"""
                 INSERT INTO {self.__pan_number}_transactions VALUES(
                    '{current_time}',
                    'deposit',
                     NULL ,
                     {balance + amount}
                 );
                 """)
        db_query(f"""
                 UPDATE customers 
                 SET account_balance = account_balance + {amount}
                 WHERE pan = '{self.__pan_number}';
                 """)
        print("Deposit Successful")
      
    def withdraw(self, amount):
        last_transac = db_query(f"""
                                SELECT account_balance FROM customers
                                WHERE pan = '{self.__pan_number}';
                                """)
        current_time = getTime()
        balance = 0
        if last_transac:
            balance = last_transac[0][0]
            
        if balance < amount:
            print("Insufficient Balance")    
            return
        else:      
            db_query(f"""
                    INSERT INTO {self.__pan_number}_transactions VALUES(
                        '{current_time}',
                        'withdrawal',
                        NULL ,
                        {balance - amount}
                    );
                    """)
            db_query(f"""
                     UPDATE customers 
                     SET account_balance = account_balance - {amount}
                     WHERE pan = '{self.__pan_number}';
                     """)
        print("Withdraw Successful")
    
    def transfer(self, pan_id, amount):
        receiver = db_query(f"""
                          SELECT * FROM customers
                          WHERE pan = '{pan_id}' ;
                          """)
        
        balance_sender = db_query(f"""
                                SELECT account_balance FROM customers
                                WHERE pan = '{self.__pan_number}';
                                """)
        
        balance_reciever = db_query(f"""
                                SELECT account_balance FROM customers
                                WHERE pan = '{pan_id}';
                                """)
        
        balance_sender = balance_sender[0][0]
        balance_reciever = balance_reciever[0][0]
        
        current_time = getTime() 
        
        if balance_sender < amount:
            print("Insufficient Balance")
            return
        
        if receiver:
            db_query(f"""
                      UPDATE customers
                      SET account_balance = account_balance + {amount }
                      WHERE pan = '{pan_id}';
                     """)
            
            db_query(f"""
                      UPDATE customers
                      SET account_balance = account_balance - {amount }
                      WHERE pan = '{self.__pan_number}';
                     """)
            
            db_query(f"""
                     INSERT INTO {self.__pan_number}_transactions VALUES(
                        '{current_time}',
                        'sent',
                        '{pan_id}' ,
                        {balance_sender - amount}
                     );
                     """)
            db_query(f"""
                     INSERT INTO {pan_id}_transactions VALUES(
                         '{current_time}',
                        'recieved',
                        '{self.__pan_number}' ,
                        {balance_reciever + amount}
                        );
                     """)
            print(f"Money transferred to {pan_id} Successfully")
        else:
            print("User Not Found ; Invalid PAN ID")
            
    def Terminate(self):
        db_query(f"""
                 UPDATE customers
                 SET status = 0
                 WHERE pan = '{self.__pan_number}';
                 """)
        print("Account Terminated Successfully")
        
    def view_transac(self):
        transactions = db_query(f"""
                                SELECT * FROM {self.__pan_number}_transactions;
                                """)
        for i in transactions:
            print(f"Time : {i[0]}     Type : {i[1]}     Counter Party Account : {i[2]}     Final Balance : {i[3]}")
            
    def update_details(self):
        option = int(input('''
                           Which field you want to change ?
                           1 : Name
                           2 : Password
                           3 : Age
                           4 : Address
                           '''))
        
        if option in (1,2,3,4):
            if option == 1:
                new_name = input("Enter the New Name : ")
                db_query(f"""
                         UPDATE customers
                         SET name = '{new_name}'
                         where pan = '{self.__pan_number}';
                         """)
                
            elif option == 2:
                new_pass = input("Enter the New Password : ")
                db_query(f"""
                         UPDATE customers
                         SET password = '{new_pass}'
                         where pan = '{self.__pan_number}';
                         """)
                
            elif option == 3:
                new_age = input("Enter the New Age : ")
                db_query(f"""
                         UPDATE customers
                         SET age = {new_age}
                         where pan = '{self.__pan_number}';
                         """)
                
            elif option == 4:
                new_add = input("Enter the New Address : ")
                db_query(f"""
                         UPDATE customers
                         SET address = '{new_add}'
                         where pan = '{self.__pan_number}';
                         """)
            print("Details updated Successfully")
        else:
            print("Invalid choice , Enter a value from the available Options only")