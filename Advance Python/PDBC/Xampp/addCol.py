import mysql.connector

try:
    con = mysql.connector.connect(host="localhost",database='pythonconnect3333', user="root", password="", port=3333)
    cursor = con.cursor()
    sql1 = "insert into students values(1,'anvesh','anvesh@gmail.com')"
    cursor.execute(sql1)
    con.commit()
    print("added record")
except Exception as e:
    print(e)
    if con:
        con.rollback()
finally:
    if cursor:
        cursor.close
    elif con:
        con.close()