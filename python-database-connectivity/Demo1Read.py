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
result = cursor.fetchall()
# print(result)
for row in result:
    print(row)

connection.close()
