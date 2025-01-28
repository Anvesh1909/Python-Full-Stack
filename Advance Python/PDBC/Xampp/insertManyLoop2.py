import mysql.connector

try:
    con = mysql.connector.connect(host="localhost",database='pythonconnect3333', user="root", password="", port=3333)
    cursor = con.cursor()
    sql1 = "insert into students values(%s,%s,%s)"
    records = []
    n = int(input("Enter the number of records: "))
    for i in range(n):
        stdid = int(input("Enter id: "))
        name = input("enter name: ")
        email = input("Enter email: ")
        records.append([stdid,name,email])
    cursor.executemany(sql1,records)
    con.commit()
    print("added many record")
except Exception as e:
    print(e)
    if con:
        con.rollback()
finally:
    if cursor:
        cursor.close
    elif con:
        con.close()