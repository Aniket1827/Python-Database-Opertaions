import mysql.connector
from mysql.connector import Error

try:
    query = "INSERT INTO Employee (Id,Name,Salary,Address) VALUES (%s,%s,%s,%s)"
    con = mysql.connector.connect(host='localhost',user='root',database='python dbc')
    cursor = con.cursor()
    records = [(103,'Rahul',3450.00,'Punjab'),
                    (104,'MSD',3000.67,'CHennai'),
                        (105,'Karthik',3580.67,'Kolkata')]
    cursor.executemany(query,records)
    con.commit()
    print("Record Inserted Successfully!")
except Error as e:
    if con:
        con.rollback()
        print("There is a problem : ",e)
finally:
    if cursor:
        cursor.close()
    if con:
        con.close()
