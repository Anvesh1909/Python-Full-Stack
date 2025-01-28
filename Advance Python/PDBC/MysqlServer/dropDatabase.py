import mysql.connector

try: 
    con = mysql.connector.connect(host="localhost", user="root", password="Anv@14078")
    cursor = con.cursor()
    sql = "drop database pythonconnect"
    cursor.execute(sql) 
    con.commit()
    print("deleted database successfully")
except Exception as e:
    print(e)
finally:
    if cursor:
        cursor.close()
    if con:
        con.close()
