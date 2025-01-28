import mysql.connector

try:
    con = mysql.connector.connect(host="localhost",user="root",password="Anv@14078",database="practice2")
    cursor = con.cursor()
    
    r = int(input("Enter id to be deleted: "))
    sql = f"delete from students where id={r}"
    cursor.execute(sql)
    con.commit()
    print("record deleted sucessfully")
    
except Exception as e:
    print(e)
    if con:
        con.rollback()
finally:
    if con:
        con.close()
    if cursor:
        cursor.close()
    