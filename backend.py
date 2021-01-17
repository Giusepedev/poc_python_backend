import mysql.connector
import os

mydb = mysql.connector.connect(
    host = os.environ['MYSQL_HOST'],
    port = os.environ['MYSQL_PORT'],
    user = os.environ['MYSQL_USER'],
    password = os.environ['MYSQL_PASSWORD'],
    database = os.environ['MYSQL_DATABASE']
)

mycursor = mydb.cursor()

sql = "UPDATE employees SET first_name = 'asdwq' WHERE employee_id = '33391'"

mycursor.execute(sql)

mydb.commit()

print(mycursor.rowcount, "record(s) affected")