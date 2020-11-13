import mysql.connector
from mysql.connector import Error

try:
    con = mysql.connector.connect(host='localhost',user='root',database='python dbc')
    cursor = con.cursor()
    updation_id = int(input("Enter Id To Update Record : "))
    new_id = int(input("Enter New Id : "))
    new_name = input("Enter New Name : ")
    new_sal = float(input("Enter New Salary : "))
    new_addr = input("Enter New Address : ")

    query="UPDATE Employee SET Id=%s, Name=%s, Salary =%s,Address=%s WHERE Id= %s"
    cursor.execute(query,(new_id,new_name,new_sal,new_addr,updation_id))
    con.commit()
    print("Record Inserted!!")
except Error as e:
    if con:
        con.rollback()
        print("There is problem ",e)
finally:
    if cursor:
        cursor.close()
    if con:
        con.close()
