import mysql.connector

try: 
    con = mysql.connector.connect(host="localhost", user="root", password="Anv@14078",database="pythonconnect")
    cursor = con.cursor()
    sql = "insert into students values(%s,%s,%s);"
    records = [(2,"Bunny1","Bunny1@gmail.com"),
               (2,"Bunny2","Bunny2@gmail.com"),
               (3,"Bunny3","Bunny3@gmail.com")]
    cursor.executemany(sql,records) 
    con.commit()
    print("records inserted sucessfully")
except Exception as e:
    print(e)
    if con:
        con.rollback()
finally:
    if cursor:
        cursor.close()
    if con:
        con.close()
