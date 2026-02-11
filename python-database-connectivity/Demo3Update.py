import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="root",
    database="isj018",
    port=3306,
)
cursor = connection.cursor()
query = "update student set name=%s, email=%s, phone=%s, address=%s where student_id=%s"
values = ("Shubham Kumar", "kumar@123.com", "12358989", "Mumbai", "5")
cursor.execute(query, values)
connection.commit()
connection.close()
print("successfully updated student")
