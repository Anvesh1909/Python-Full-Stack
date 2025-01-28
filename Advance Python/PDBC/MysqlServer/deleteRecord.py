import mysql.connector

try: 
    con = mysql.connector.connect(host="localhost", user="root", password="Anv@14078",database="pythonconnect")
    cursor = con.cursor()
    sql = "delete from students where id=134"
    cursor.execute(sql) 
    con.commit()
    print("record deleted sucessfully")
except Exception as e:
    print(e)
    if con:
        con.rollback()
finally:
    if cursor:
        cursor.close()
    if con:
        con.close()
