import mysql.connector

try:
    con = mysql.connector.connect(host="localhost", user="root", password="", port=3333)
    cursor = con.cursor()
    sql1 = "use pythonconnect3333"
    sql2 = "create table students(id int,name varchar(20))"
    cursor.execute(sql1)
    cursor.execute(sql2)
    print("table created")

except Exception as e:
    print(e)
    if con:
        con.rollback()
finally:
    if cursor:
        cursor.close()
    elif con:
        con.close()