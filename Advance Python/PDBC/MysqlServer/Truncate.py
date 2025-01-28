import mysql.connector

try: 
    con = mysql.connector.connect(host="localhost", user="root", password="Anv@14078",database="pythonconnect")
    cursor = con.cursor()
    sql = "truncate table students;"
    cursor.execute(sql) 
    print("all records are deleted permenently")
except Exception as e:
    print(e)
finally:
    if cursor:
        cursor.close()
    if con:
        con.close()
