import mysql.connector

try:
    
    con = mysql.connector.connect(host="localhost" ,user="root",password="Anv@14078",database="practice2")
    cursor = con.cursor()
    sql = "insert into students values(%s,%s,%s);"
    records = [(4,"bunny","bunny@gmail.com"),(5,"bunny2","bunny2@gmail.com"),(6,"bunny3","bunny3@gmail.com")]
    
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