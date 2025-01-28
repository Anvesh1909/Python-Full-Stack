import mysql.connector

# ddl commade(data defination language)
try:
    
    con = mysql.connector.connect(host="localhost" ,user="root",password="Anv@14078",database="practice2")
    cursor = con.cursor()
    sql = "truncate table students;"
    cursor.execute(sql)
    print("table trucated successfully")
    
except Exception as e:
    print(e)
finally:
    if con:
        con.close()
    if cursor:
        cursor.close