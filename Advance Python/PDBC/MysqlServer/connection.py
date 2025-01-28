import mysql.connector

try: 
    con = mysql.connector.connect(host="localhost", user="root", password="Anv@14078")
    cursor = con.cursor()
    sql = "create database pythonConnect"
    cursor.execute(sql) 
    print("A database is created successfully inside MySQL")
except Exception as e:
    print(e)
finally:
    if cursor:
        cursor.close()
    if con:
        con.close()
