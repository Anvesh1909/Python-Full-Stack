Here are the solutions to all the questions using **Python and MySQL Connector**.

---

## **1. Insert Multiple Rows Using executemany()**
```python
import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="your_username",
    password="your_password",
    database="python_db"
)
cursor = conn.cursor()

sql_insert_query = "INSERT INTO Laptop (Id, Name, Price, Purchase_date) VALUES (%s, %s, %s, %s)"
records_to_insert = [
    (4, 'HP Pavilion Power', 1999, '2019-01-11'),
    (5, 'MSI WS75 9TL-496', 5799, '2019-02-27'),
    (6, 'Microsoft Surface', 2330, '2019-07-23')
]

cursor.executemany(sql_insert_query, records_to_insert)
conn.commit()
print(f"{cursor.rowcount} Records inserted successfully.")

cursor.close()
conn.close()
```

---

## **2. Insert Timestamp and DateTime**
```python
from datetime import datetime

cursor = conn.cursor()
sql_insert_query = "INSERT INTO Laptop (Id, Name, Price, Purchase_date) VALUES (%s, %s, %s, %s)"
record = (7, 'Acer Predator Triton', 2435, datetime.now())

cursor.execute(sql_insert_query, record)
conn.commit()
print("Timestamp Inserted Successfully.")

cursor.close()
conn.close()
```

---

## **3. Fetch Single Row Using fetchone()**
```python
cursor = conn.cursor()
cursor.execute("SELECT * FROM Laptop")
record = cursor.fetchone()

print("Printing first record:", record)

cursor.close()
conn.close()
```

**Output:**
```
Printing first record: (1, 'Lenovo ThinkPad P71', 6459.0, datetime.date(2019, 8, 14))
```

---

## **4. Fetch Data Using Column Names**
```python
cursor = conn.cursor(dictionary=True)
cursor.execute("SELECT * FROM Laptop")
records = cursor.fetchall()

print("Fetching each row using column name")
for row in records:
    print(row["Id"], row["Name"], row["Price"], row["Purchase_date"])

cursor.close()
conn.close()
```

---

## **5. Update Multiple Rows**
```python
sql_update_query = "UPDATE Laptop SET Price = %s WHERE Id = %s"
update_values = [(5000, 4), (6000, 5)]

cursor.executemany(sql_update_query, update_values)
conn.commit()
print(f"{cursor.rowcount} Records updated successfully.")

cursor.close()
conn.close()
```

---

## **6. Update Datetime Column**
```python
sql_update_query = "UPDATE Laptop SET Purchase_date = %s WHERE Id = %s"
update_values = [(datetime.now(), 4), (datetime.now(), 5)]

cursor.executemany(sql_update_query, update_values)
conn.commit()
print("Purchased Date Updated Successfully.")

cursor.close()
conn.close()
```

---

## **7. Delete All Rows Using TRUNCATE**
```python
cursor = conn.cursor()
cursor.execute("TRUNCATE TABLE Laptop")
conn.commit()
print("All Records Deleted Successfully.")

cursor.close()
conn.close()
```

---

## **8. Delete Table and Database**
```python
cursor = conn.cursor()
cursor.execute("DROP TABLE IF EXISTS Laptop")
cursor.execute("DROP DATABASE IF EXISTS python_db")
conn.commit()
print("Table and Database Deleted Successfully.")

cursor.close()
conn.close()
```

---

## **9. Delete a Column from a Table**
```python
cursor = conn.cursor()
cursor.execute("ALTER TABLE Laptop DROP COLUMN Price")
conn.commit()
print("Column Deleted Successfully.")

cursor.close()
conn.close()
```

---

These solutions execute all required queries using Python and MySQL. Let me know if you need further modifications! 🚀