import mysql.connector
from mysql.connector import Error

try:
  con =mysql.connector.connect(host='localhost',user='root',database='python dbc')
  cursor = con.cursor()
  while True:
      Id = int(input("Enter Id : "))
      Name = input("Enter Name : ")
      Salary = float(input("Enter Salary : "))
      Address = input("Enter Address : ")
      query = "INSERT INTO Employee (Id,Name,Salary,Address) VALUES (%s, %s, %s, %s)"
      cursor.execute(query,(Id,Name,Salary,Address))
      con.commit()
      print("Record Inserted!!")
      option = input("Do You Want To Add More Records (y|n) : ")
      if option.lower() == 'n':
          break
except Error as e:
    if con:
        con.rollback()
        print("There is problem ",e)
finally:
    if cursor:
        cursor.close()
    if con:
        con.close()
