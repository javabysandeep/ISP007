import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="root",
    database="isj018",
    port=3306,
)
cursor = connection.cursor()
query = "delete from student where student_id=%s"
cursor.execute(query, ("5",))
connection.commit()
connection.close()
print("successfully deleted student")
