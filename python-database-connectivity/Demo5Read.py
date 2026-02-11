import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="root",
    database="hr",
    port=3306,
)
cursor = connection.cursor()
cursor.execute("select * from employees")
one_row = cursor.fetchone()
print(one_row)


connection.close()
