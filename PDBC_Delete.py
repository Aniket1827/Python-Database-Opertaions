import mysql.connector
from mysql.connector import Error

try:
    #con = mysql.connector.connect(host='localhost',user='root',database='python db')
    con = mysql.connector.connect(host='localhost',user='root',database='python dbc')
    cursor = con.cursor()
    delete_id = int(input("Enter Id To Delete : "))
    query = "DELETE FROM Employee WHERE Id=%s"
    cursor.execute(query,(delete_id,))
    con.commit()
    print("Record Deleted Successfully!!")
except Error as e:
    if con:
        con.rollback()
        print("There is a problem ",e)
finally:
    if cursor:
        cursor.close()
    if con:
        con.close()
