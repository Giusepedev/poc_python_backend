import mysql.connector
import os

mydb = mysql.connector.connect(
    host = "127.0.0.1",
    port = "3306",
    user = "root",
    password = os.environ['password'],
    database = "sql_hr"
)

mycursor = mydb.cursor()

sql = "UPDATE employees SET first_name = 'julia' WHERE employee_id = '33391'"

mycursor.execute(sql)

mydb.commit()

print(mycursor.rowcount, "record(s) affected")