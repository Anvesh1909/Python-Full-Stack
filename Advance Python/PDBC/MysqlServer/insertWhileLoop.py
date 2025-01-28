import mysql.connector

try: 
    con = mysql.connector.connect(host="localhost", user="root", password="Anv@14078",database="pythonconnect")
    cursor = con.cursor()
    sql = "insert into students values(%s,%s,%s);"
    records = []
    
    n = int(input("Enter number of records: "))
    while n>0:
        stdid = int(input("Enter student id: "))
        name = input("Enter student name: ")
        email = input("Enter email: ")
        records.append((stdid,name,email))
        n-=1
        
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
