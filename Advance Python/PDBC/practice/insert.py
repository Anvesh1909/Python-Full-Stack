import mysql.connector

try:
    
    con = mysql.connector.connect(host="localhost" ,user="root",password="Anv@14078",database="practice2")
    cursor = con.cursor()
    sql = "insert into students values(3,'Anvesh3','anvesh3@gmail.com');"
    cursor.execute(sql)
    # 100//0
    print("record inserted sucessfully")
    con.commit()
except Exception as e:
    print(e)
    if con:
        # print("roolback")
        con.rollback()
finally:
    if con:
        con.close()
    if cursor:
        cursor.close