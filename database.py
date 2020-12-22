import sqlite3
import csv

def print_DB():
    try:
        result = theCursor.execute("SELECT id, FName, LName, Age, Address, Salary, HireDate FROM Employees")
        for row in result:
            print("ID :", row[0])
            print("FName :", row[1])
            print("LName :", row[2])
            print("Age :", row[3])
            print("Address :", row[4])
            print("Salary :", row[5])
            print("HireDate :", row[6])
    except sqlite3.OperationError:
        print("The table doesn't exist")
    except:
        print("Couldn't get data")

db_conn = sqlite3.connect("test.db")

print("Database Created")

theCursor = db_conn.cursor()
# execute() executes a SQL command
# We organize our data in tables by defining their
# name and the data type for the data

# We define the table name
# A primary key is a unique value that differentiates
# each row of data in our table
# The primary key will auto increment each time we
# add a new Employee
# If a piece of data is marked as NOT NULL, that means
# it must have a value to be valid

# NULL is NULL and stands in for no value
# INTEGER is an integer
# TEXT is a string of variable length
# REAL is a float
# BLOB is used to store binary data

# You can delete a table if it exists like this
# db_conn.execute("DROP TABLE IF EXISTS Employees")
# db_conn.commit()
try:
    db_conn.execute("CREATE TABLE Employees(ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, FName TEXT NOT NULL, LName TEXT NOT NULL, Age INT NOT NULL, \
    Address TEXT, Salary REAL, HireDate TEXT);")
    db_conn.commit()
    print("Table Created")
except sqlite3.OperatorationError:
    print("Table not Created")

# To insert data into a table we use INSERT INTO
# followed by the table name and the item name
# and the data to assign to those items

db_conn.execute("INSERT INTO Employees (FName, LName, Age, Address, Sa  lary, HireDate)"
                "VALUES ('Kaney', 'Nguyen', 41, '123 Main St', '500,000', date('now'))")

db_conn.commit()
print_DB()
db_conn.close()

