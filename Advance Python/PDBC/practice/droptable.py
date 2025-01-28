import mysql.connector

try:
    
    con = mysql.connector.connect(host="localhost" ,user="root",password="Anv@14078",database="practice2")
    cursor = con.cursor()
    sql = "drop table students"
    cursor.execute(sql)
    print("table dropped")
    
except Exception as e:
    print(e)
finally:
    if con:
        con.close()
    if cursor:
        cursor.close