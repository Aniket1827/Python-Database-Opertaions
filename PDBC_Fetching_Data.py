import mysql.connector
from mysql.connector import Error

try:
     con = mysql.connector.connect(host='localhost',user='root',database='python dbc')
     cursor = con.cursor()
     query = "SELECT * FROM Employee"
     cursor.execute(query)
     row = cursor.fetchone()
     while row is not None:
         print("Id : ",row[0])
         print("Name : ",row[1])
         print("Salary : ",row[2])
         print("Address : ",row[3])
         print()
         row = cursor.fetchone()
except Error as e:
    if con:
        print("There is problem ",e)
finally:
    if cursor:
        cursor.close()
    if con:
        con.close()
