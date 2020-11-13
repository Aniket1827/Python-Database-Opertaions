import mysql.connector
from mysql.connector import Error

try:
    #con = mysql.connector.connect(host='localhost',user='root',database='python dbc')
    con = mysql.connector.connect(host='localhost',user='root',database='python dbc')
    cursor = con.cursor()
    query = "SELECT * FROM Employee"
    cursor.execute(query)
    n = int(input("Enter Number Of Rows: "))
    data = cursor.fetchmany(n)
    f = open('dbreords.txt','w')
    f.write(str(data))
    print()
    print("Data Inserted!!")
except Error as e:
    if con:
        print("There is a problem ",e)
finally:
    if cursor:
        cursor.close()
    if con:
        con.close()
