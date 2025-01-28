import mysql.connector

try:
    con = mysql.connector.connect(
        host="localhost", database='pythonconnect3333', user="root", password="", port=3333)
    cursor = con.cursor()
    n = int(input("Enter the number of records: "))
    for i in range(n):
        stdid = int(input("Enter id: "))
        name = input("Enter name: ")
        email = input("Enter email: ")
        sql1 = 'INSERT INTO students (id, name, email) VALUES (%s, %s, %s)'
        cursor.execute(sql1, (stdid, name, email))
        con.commit()
    print("Records added successfully")
except Exception as e:
    print(e)
    if con:
        con.rollback()
finally:
    if cursor:
        cursor.close()
    if con:
        con.close()
