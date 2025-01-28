import mysql.connector

try:
    
    con = mysql.connector.connect(host="localhost" ,user="root",password="Anv@14078")
    cursor = con.cursor()
    sql = "create database practice2;"
    cursor.execute(sql)
    print("database created suessfully")
    
except Exception as e:
    print(e)
finally:
    if con:
        con.close()
    if cursor:
        cursor.close