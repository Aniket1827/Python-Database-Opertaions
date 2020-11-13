import mysql.connector
from mysql.connector import Error

try:
    query = """INSERT INTO Employee VALUES
                (101,'Virat',1250.00,'Banglore'),
                (102,'Rohit',3000.67,'Mumbai')"""
    con = mysql.connector.connect(host='localhost',user='root',database='python dbc')
    cursor = con.cursor()
    cursor.execute(query)
    con.commit()  #IMPORTANT Line to be added so that record gets inserted unlike JDBC
    print("Data Inserted!")
except Error as e:
    if con:
        con.rollback()
        print("There is problem : ",e)
finally:
    if cursor:  #meanin if con!=None
        cursor.close()
    if con:
        con.close()
