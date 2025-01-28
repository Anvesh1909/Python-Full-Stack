import mysql.connector

try:
    
    con = mysql.connector.connect(host="localhost" ,user="root",password="",port=3333)
    cursor = con.cursor()
    sql = "use practice2;"
    cursor.execute(sql)
    print("selected database")
    
except Exception as e:
    print(e)
finally:
    if con:
        con.close()
    if cursor:
        cursor.close