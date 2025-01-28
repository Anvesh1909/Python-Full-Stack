import mysql.connector

try:
    
    con = mysql.connector.connect(host="localhost" ,user="root",password="",database="practice2",port=3333)
    cursor = con.cursor()
    sql = "insert into students values(%s,%s,%s);"
    
    n = int(input("Enter no of records: "))
    for i in range(n):
        stdid = int(input("Enter student id: "))
        name = input("Enter name: ")
        email = input("Enter email: ")
        cursor.execute(sql,(stdid,name,email))
        con.commit()
        print("record inserted sucessfully")
    
except Exception as e:
    print(e)
    if con:
        con.rollback()
finally:
    if con:
        con.close()
    if cursor:
        cursor.close