import mysql.connector

try: 
    con = mysql.connector.connect(host="localhost", user="root", password="Anv@14078",database="pythonconnect")
    cursor = con.cursor()
    sql = "select * from students;"
    
    cursor.execute(sql)
    data = cursor.fetchall() 
    
    print("id\t\tname\t\temail")
    print("================================================")
    # print(data)
    for i in data:
        # print(i)
        for j in i:
            print(j,end="\t\t")
        print()
    
    
    print("students fetched sucessfully")
except Exception as e:
    print(e)
finally:
    if cursor:
        cursor.close()
    if con:
        con.close()
