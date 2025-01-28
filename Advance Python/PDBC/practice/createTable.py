import mysql.connector

try:
    
    con = mysql.connector.connect(host="localhost" ,user="root",password="Anv@14078",database="practice2")
    cursor = con.cursor()
    sql = "create table students(id int, name varchar(100), email varchar(100));"
    cursor.execute(sql)
    print("created table sucessfully")
    
except Exception as e:
    print(e)
finally:
    if con:
        con.close()
    if cursor:
        cursor.close