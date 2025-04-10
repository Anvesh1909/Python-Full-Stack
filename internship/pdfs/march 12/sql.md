Here are the Python implementations for all the tasks in the assignment using **MySQL Connector**:

### **Setup: Install MySQL Connector**
Ensure you have installed the MySQL connector:
```bash
pip install mysql-connector-python
```

### **Connect to the MySQL Database**
```python
import mysql.connector
from datetime import date

# Establish a connection
conn = mysql.connector.connect(
    host="localhost",
    user="your_username",
    password="your_password",
    database="python_db"
)
cursor = conn.cursor()
```

---

## **1. Fetch Database Server Version**
```python
def get_db_version():
    cursor.execute("SELECT VERSION()")
    version = cursor.fetchone()
    print("Database Version:", version[0])

get_db_version()
```

---

## **2. Fetch Hospital and Doctor Information**
```python
def get_hospital_detail(hospital_id):
    query = "SELECT * FROM Hospital WHERE Hospital_Id = %s"
    cursor.execute(query, (hospital_id,))
    result = cursor.fetchone()
    if result:
        print(f"Hospital ID: {result[0]}, Name: {result[1]}, Bed Count: {result[2]}")
    else:
        print("Hospital not found.")

def get_doctor_detail(doctor_id):
    query = "SELECT * FROM Doctor WHERE Doctor_Id = %s"
    cursor.execute(query, (doctor_id,))
    result = cursor.fetchone()
    if result:
        print(f"Doctor ID: {result[0]}, Name: {result[1]}, Hospital ID: {result[2]}, Joining Date: {result[3]}, Speciality: {result[4]}, Salary: {result[5]}, Experience: {result[6]}")
    else:
        print("Doctor not found.")

get_hospital_detail(2)
get_doctor_detail(105)
```

---

## **3. Get List of Doctors Based on Specialty & Salary**
```python
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
```

---

## **4. Get List of Doctors from a Given Hospital**
```python
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
```

---

## **5. Update Doctor Experience**
```python
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
    conn.commit()
    
    print(f"Updated Experience for Doctor {doctor_id}: {experience} years")

update_doctor_experience(101)
```

---

### **Close the Database Connection**
```python
cursor.close()
conn.close()
```

These implementations:
- Connect to the database
- Fetch and display requested information
- Update doctor experience dynamically
- Use parameterized queries to prevent SQL injection

Would you like any modifications or explanations? 🚀