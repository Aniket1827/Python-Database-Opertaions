import mysql.connector
from mysql.connector import Error

try:
    query = """CREATE TABLE Employee (
                             Id int(11) NOT NULL,
                             Name varchar(20) NOT NULL,
                             Salary float NOT NULL,
                             Address varchar(20) NOT NULL) """
    con = mysql.connector.connect(host='localhost',user='root',database='python dbc')
    cursor = con.cursor()
    cursor.execute(query)
    print("Table Created")
except Error as e:
    if con:
        con.rollback()
        print("There is problem ",e)
finally:
    if cursor:
        cursor.close()
    if con:
        con.close()
