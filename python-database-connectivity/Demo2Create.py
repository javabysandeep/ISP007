import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="root",
    database="isj018",
    port=3306,
)
cursor = connection.cursor()
query = "insert into student(student_id,name,email,phone, address) values(%s,%s, %s, %s, %s)"
values = ("5", "Shubham", "1234@gmail.com", "123", "Pune")
cursor.execute(query, values)
connection.commit()
connection.close()
print("successfully added student")
