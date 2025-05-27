import mysql.connector as sql

mydb = sql.connect(
    host="localhost",
    user="root",
    passwd="LoveYou3000$",
    database="bank"
)
cursor = mydb.cursor()

def db_query(query):
    cursor.execute(query)
    if query.strip().upper().startswith("SELECT"):
        return cursor.fetchall()
    else:
        mydb.commit()



def create_customer_table():
    cursor.execute('''
                     CREATE TABLE IF NOT EXISTS customers(
                         pan varchar(10) PRIMARY KEY,
                         name varchar(20) NOT NULL,
                         account_number INTEGER NOT NULL,
                         account_balance INTEGER ,
                         password char(10) NOT NULL,
                         age INTEGER NOT NULL,
                         sex char(1) NOT NULL,
                         address varchar(50) NOT NULL,
                         status boolean NOT NULL
                     )
                     
                     ''')

    mydb.commit()

if __name__ == "__main__":
    create_customer_table()