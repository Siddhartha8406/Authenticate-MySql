#TestDB

import random
import mysql.connector

db=mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'root',
    database = 'TestDB'
)

myCursor = db.cursor()

#myCursor.execute("CREATE TABLE Vault(userName varchar(50) NOT NULL, pass varchar(50)NOT NULL, recoveryKey varchar(50))")

def add(uname, password, key):
    myCursor.execute(f"INSERT INTO Vault(userName, pass, recoveryKey) VALUES('{uname}','{password}','{key}')")
    db.commit()

#add('Rashmi', 'test1234', 'hdf')

def check(uname):
    myCursor.execute(f"SELECT * FROM VAULT WHERE userName = '{uname}'")
    value = False
    for i in myCursor:
        print(i)
        if i != '':
            value = True
            break
    return value

print(check('rashmi'))