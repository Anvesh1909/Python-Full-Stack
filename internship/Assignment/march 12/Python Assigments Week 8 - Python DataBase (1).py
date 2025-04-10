

# 1
import mysql.connector

try: 
    con = mysql.connector.connect(host="localhost" ,user="root",password="Anv@14078")
    cursor = con.cursor()
    sql = 'Create Database python_db'
    cursor.execute(sql)
    print("Database created successfully")

except Exception as e:
    print(e)
finally:
    if con:
        con.close()
    if cursor:
        cursor.close()


# 2

import mysql.connector

try: 
    con = mysql.connector.connect(host="localhost" ,user="root",password="Anv@14078", database='python_db')
    cursor = con.cursor()
    sql = '''CREATE TABLE Hospital ( 
    Hospital_Id INT UNSIGNED NOT NULL,  
    Hospital_Name TEXT NOT NULL,  
    Bed_Count INT,  
    PRIMARY KEY (Hospital_Id));'''
    cursor.execute(sql)
    print("Table created successfully")

except Exception as e:
    print(e)
finally:
    if con:
        con.close()
    if cursor:
        cursor.close()




import mysql.connector

try: 
    con = mysql.connector.connect(host="localhost" ,user="root",password="Anv@14078", database='python_db')
    cursor = con.cursor()
    sql = '''INSERT INTO Hospital (Hospital_Id, Hospital_Name, Bed_Count)  
VALUES  
('1', 'Mayo Clinic', 200),  
('2', 'Cleveland Clinic', 400),  
('3', 'Johns Hopkins', 1000),  
('4', 'UCLA Medical Center', 1500);'''
    cursor.execute(sql)
    con.commit()
    print("Values inserted successfully")

except Exception as e:
    print(e)
finally:
    if con:
        con.close()
    if cursor:
        cursor.close()





# 3
import mysql.connector

try: 
    con = mysql.connector.connect(host="localhost" ,user="root",password="Anv@14078", database='python_db')
    cursor = con.cursor()
    sql = '''CREATE TABLE Doctor ( 
    Doctor_Id INT UNSIGNED NOT NULL, 
    Doctor_Name TEXT NOT NULL,  
    Hospital_Id INT NOT NULL,  
    Joining_Date DATE NOT NULL,  
    Speciality TEXT NULL,  
    Salary INT NULL,  
    Experience INT NULL,  
    PRIMARY KEY (Doctor_Id) 
); 
 
'''
    cursor.execute(sql)
    print("Table inserted successfully")

except Exception as e:
    print(e)
finally:
    if con:
        con.close()
    if cursor:
        cursor.close()


import mysql.connector

try: 
    con = mysql.connector.connect(host="localhost" ,user="root",password="Anv@14078", database='python_db')
    cursor = con.cursor()
    sql = '''INSERT INTO Doctor (Doctor_Id, Doctor_Name, Hospital_Id, Joining_Date, Speciality, Salary, 
Experience)  
VALUES  
('101', 'David', '1', '2005-2-10', 'Pediatric', '40000', NULL),  
('102', 'Michael', '1', '2018-07-23', 'Oncologist', '20000', NULL),  
('103', 'Susan', '2', '2016-05-19', 'Garnacologist', '25000', NULL),  
('104', 'Robert', '2', '2017-12-28', 'Pediatric ', '28000', NULL),  
('105', 'Linda', '3', '2004-06-04', 'Garnacologist', '42000', NULL),  
('106', 'William', '3', '2012-09-11', 'Dermatologist', '30000', NULL),  
('107', 'Richard', '4', '2014-08-21', 'Garnacologist', '32000', NULL),  
('108', 'Karen', '4', '2011-10-17', 'Radiologist', '30000', NULL); '''
    cursor.execute(sql)
    con.commit()
    print("Values inserted successfully")

except Exception as e:
    print(e)
finally:
    if con:
        con.close()
    if cursor:
        cursor.close()









# 1
import mysql.connector

try: 
    con = mysql.connector.connect(host="localhost" ,user="root",password="Anv@14078", database='python_db')
    cursor = con.cursor()
    cursor.execute("SELECT VERSION()")
    version = cursor.fetchone()
    print("Database Version:", version[0])
except Exception as e:
    print(e)
finally:
    if con:
        con.close()
    if cursor:
        cursor.close()




# 2


import mysql.connector


con = mysql.connector.connect(host="localhost" ,user="root",password="Anv@14078", database='python_db')
cursor = con.cursor()

def get_hospital_details(hospital_id):
    query = "SELECT * FROM Hospital WHERE Hospital_Id = %s"
    cursor.execute(query, (hospital_id,))
    result = cursor.fetchone()
    if result:
        print(f"Hospital ID: {result[0]}\n Name: {result[1]}\n Bed Count: {result[2]} \n\n")
    else:
        print("Hospital not found.")

def get_doctor_details(doctor_id):
    query = "SELECT * FROM Doctor WHERE Doctor_Id = %s"
    cursor.execute(query, (doctor_id,))
    result = cursor.fetchone()
    if result:
        print(f"Doctor ID: {result[0]}\n Name: {result[1]}\n Hospital ID: {result[2]}\n Joining Date: {result[3]}\n Speciality: {result[4]}\n Salary: {result[5]}\n Experience: {result[6]} \n\n")
    else:
        print("Doctor not found.")

get_hospital_details(2) 
get_doctor_details(105)


cursor.close()
con.close()




# 3
import mysql.connector


con = mysql.connector.connect(host="localhost" ,user="root",password="Anv@14078", database='python_db')
cursor = con.cursor()

def get_specialist_doctors_list(speciality, salary):
    query = "SELECT * FROM Doctor WHERE Speciality = %s AND Salary > %s"
    cursor.execute(query, (speciality, salary))
    results = cursor.fetchall()
    
    if results:
        for row in results:
            print(f"Doctor ID: {row[0]}, Name: {row[1]}, Salary: {row[5]}")
    else:
        print("No doctors found matching criteria.")

get_specialist_doctors_list("Garnacologist", 30000)

cursor.close()
con.close()




# 4
import mysql.connector


con = mysql.connector.connect(host="localhost" ,user="root",password="Anv@14078", database='python_db')
cursor = con.cursor()

def get_doctors(hospital_id):
    query1 = "SELECT Hospital_Name FROM Hospital WHERE Hospital_Id = %s"
    cursor.execute(query1, (hospital_id,))
    hospital_name = cursor.fetchone()
    
    if not hospital_name:
        print("Hospital not found.")
        return
    
    print(f"Hospital: {hospital_name[0]}")
    
    query2 = "SELECT Doctor_Id, Doctor_Name, Speciality, Salary FROM Doctor WHERE Hospital_Id = %s"
    cursor.execute(query2, (hospital_id,))
    doctors = cursor.fetchall()
    
    if doctors:
        for doc in doctors:
            print(f"Doctor ID: {doc[0]}, Name: {doc[1]}, Speciality: {doc[2]}, Salary: {doc[3]}")
    else:
        print("No doctors found in this hospital.")

get_doctors(2)

cursor.close()
con.close()


# 5

import mysql.connector
from datetime import date

con = mysql.connector.connect(host="localhost" ,user="root",password="Anv@14078", database='python_db')
cursor = con.cursor()

def update_doctor_experience(doctor_id):
    query = "SELECT Joining_Date FROM Doctor WHERE Doctor_Id = %s"
    cursor.execute(query, (doctor_id,))
    result = cursor.fetchone()
    
    if not result:
        print("Doctor not found.")
        return
    
    joining_date = result[0]
    today = date.today()
    experience = today.year - joining_date.year
    
    update_query = "UPDATE Doctor SET Experience = %s WHERE Doctor_Id = %s"
    cursor.execute(update_query, (experience, doctor_id))
    con.commit()
    
    print(f"Updated Experience for Doctor {doctor_id}: {experience} years")

update_doctor_experience(101)

cursor.close()
con.close()