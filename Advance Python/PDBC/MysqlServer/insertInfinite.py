import mysql.connector

try: 
    con = mysql.connector.connect(host="localhost", user="root", password="Anv@14078",database="pythonconnect")
    cursor = con.cursor()
    sql = "insert into students values(%s,%s,%s);"
    
    while True:
        stdid = int(input("Enter student id: "))
        name = input("Enter student name: ")
        email = input("Enter email: ")

        cursor.execute(sql,(stdid,name,email)) 
        con.commit()
        print("record inserted sucessfully")
        option = input("Do you want to insert another [yes:no]: ")
        if option=="no":
            break    
    
except Exception as e:
    print(e)
    if con:
        con.rollback()
finally:
    if cursor:
        cursor.close()
    if con:
        con.close()
