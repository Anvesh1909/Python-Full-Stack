import mysql.connector

try: 
    con = mysql.connector.connect(host="localhost", user="root", password="Anv@14078",database="pythonconnect")
    cursor = con.cursor()
    sql = "insert into students values(%s,%s,%s);"
    
    n = int(input("Enter number of records: "))
    for i in range(n):
        stdid = int(input("Enter student id: "))
        name = input("Enter student name: ")
        email = input("Enter email: ")

        cursor.execute(sql,(stdid,name,email)) 
        con.commit()
        print("record inserted sucessfully")
        
except Exception as e:
    print(e)
    if con:
        con.rollback()
finally:
    if cursor:
        cursor.close()
    if con:
        con.close()
