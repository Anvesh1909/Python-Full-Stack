import mysql.connector

try:
    
    con = mysql.connector.connect(host="localhost" ,user="root",password="",database="practice2",port=3333)
    cursor = con.cursor()
    sql = "insert into students values(%s,%s,%s);"
    records = []
    
    n = int(input("Enter number of records: "))
    for i in range(n):
        stdid = int(input("Enter student id: "))
        name = input("Enter name: ")
        email = input("Enter email: ")
        records.append((stdid,name,email))
    
    cursor.executemany(sql,records)
    print("records inserted sucessfully")
    con.commit()
except Exception as e:
    print(e)
    if con:
        con.rollback()
finally:
    if con:
        con.close()
    if cursor:
        cursor.close