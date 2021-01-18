import mysql.connector
import os
from flask import Flask, json

mydb = mysql.connector.connect(
    host = os.environ['MYSQL_HOST'],
    port = os.environ['MYSQL_PORT'],
    user = os.environ['MYSQL_USER'],
    password = os.environ['MYSQL_PASSWORD'],
    database = os.environ['MYSQL_DATABASE']
)



#sql = "UPDATE employees SET first_name = 'asdwq' WHERE employee_id = '33391'"




#mydb.commit()

#print(mycursor.rowcount, "record(s) affected")



api = Flask(__name__)

@api.route('/employees', methods=['GET'])
def get_employees():
    mycursor = mydb.cursor()
    sql = "SELECT * FROM employees"
    mycursor.execute(sql)
    employees = mycursor.fetchall()
    return json.dumps(employees)

if __name__ == '__main__':
    api.run(host=os.environ['URL'], port=os.environ['PORT'])