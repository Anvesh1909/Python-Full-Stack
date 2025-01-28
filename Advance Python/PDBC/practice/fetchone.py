import mysql.connector

try:
    con = mysql.connector.connect(host="localhost",user="root",password="Anv@14078",database="practice2")
    cursor = con.cursor()
    
    sql = "select * from students where id=1;"
    cursor.execute(sql)
    data = cursor.fetchone()
    
    print(data)
    # for i in data:
    #     # print(i)
    #     for j in i:
    #         print(j,end="\t")
    #     print()
        
except Exception as e:
    print(e)
finally:
    if con:
        con.close()
    if cursor:
        cursor.close()
