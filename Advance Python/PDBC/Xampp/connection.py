import mysql.connector

try: 
    sql_1 = "create database pythonConnect3333"
    con = mysql.connector.connect(host="localhost", user="root", password="", port=3333)
    cursor = con.cursor()
    cursor.execute(sql_1) 
    print("A database is created successfully inside MySQL")
except Exception as e:
    print(e)
finally:
    if cursor:
        cursor.close()
    if con:
        con.close()
