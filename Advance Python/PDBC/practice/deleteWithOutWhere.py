import mysql.connector

try:
    con = mysql.connector.connect(host="localhost",user="root",password="Anv@14078",database="practice2")
    cursor = con.cursor()
    
    sql = "truncate table students;"
    # sql = "delete from students;"
    cursor.execute(sql)
    
    con.rollback()
    
    con.commit()
    print("record deleted sucessfully")
    
except Exception as e:
    print(e)
    if con:
        con.rollback()
finally:
    if con:
        con.close()
    if cursor:
        cursor.close()
    