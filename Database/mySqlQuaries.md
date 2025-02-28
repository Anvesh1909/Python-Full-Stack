# Sql Quaries

- `SHOW DATABASES;` to show all databases 
```sql
mysql> show databases;
+------------------------------+
| Database                     |
+------------------------------+
| accident_notification        |
| djangocon                    |
| employees                    |
| identifying_student_profiles |
| information_schema           |
| mysql                        |
| nbkr                         |
| performance_schema           |
| practice2                    |
+------------------------------+
9 rows in set (0.10 sec)

```
- `SELECT DATABASE();` to know the current database 
```sql 
mysql> select database();
+------------+
| database() |
+------------+
| NULL       |
+------------+
1 row in set (0.01 sec)
```
- `USE databaseName;` to use database 
- `SHOW TABLES;` to show tables inside the database 
- `DESC tableName;` to know the structure and information about the table 

## SELECT quary 
- `SELECT * FROM tableName;` to show data inside the table
- `SELECT * FROM tableName LIMIT 5;` to show only 5 records
    - here `*` means to select all the coloums
- `SELECT col1,col2,col3 FROM tableName;` to select only some coloums
---
## Types of commands in sql
1. DDL (Data definition language)
2. DML (Data manipulation language)
3. DQL / DRL (Data quary or retrival language)
4. TCL (Transaction control language)
5. DCL (Data control language)
6. Utility Commands

---
### Data definition language (DDL) commands
- used to define or modiffy the structure of the database and its objects(table, indexes etc)
- create database, tables
- delete database, tables
- manipulate the structure of table
- these commands work at the schema level (which means database level)
- `CREATE` , `ALTER`, `DROP`, `TRUNCATE` , `RENAME`
- `CREATE` - used to create databases, tables , indexes  

```sql

SHOW DATABASES;

CREATE DATABASE databaseName;

-- Cretaes if not available 
CREATE DATABASE IF NOT EXISTS databaseName;

USE databaseName;

-- to know the current database selected
SELECT DATABASE();

SHOW TABLES;

-- To delete database
DROP DATABASE databaseName;

-- delete database if available
DROP DATABASE IF EXISTS databaseName;

-- to create table syntax
CREATE TABLE tableName(
    coloum1 datatype,
    coloum2 datatype,
    ...
    ...
);

-- to create table
CREATE TABLE employees(
    empId INT,
    ename VARCHAR(30),
    salary INT,
    city VARCHAR(30)
);


-- to show the structure of the table 
-- DESC tableName;
DESC employees;


-- to show the records inside the table;
-- SELECT * FROM tableName;
SELECT * FROM employees;



```

---
## Alter 
- is used to add, delete, modify coloums, add or remove the constrains in an existing table 
```sql

-- add colume
ALTER TABLE tableName ADD COLOUMN colName datatype;

-- to show the updated structure of the table
DESC tableName;

-- to modift the existing coloum
ALTER TABLE tableName MODIFY COLOUMN colName datatype;

-- to delete coloum
ALTER TABLE tableName DROP COLOUMN colName;

-- deleting the table
-- DROP TABLE tableName;
DROP TABLE employees;

-- drop multiple tables
DROP TABLE table1, table2, ... ;


```

# Data Manipulation Language (DML)
```sql

CREATE DATABASE IHUB;

CREATE DATABASE IF NOT EXISTS IHUB;

USE IHUB;

CREATE TABLE employees(
    empId INT,
    ename VARCHAR(30),
    salary INT,
    city VARCHAR(30)
);

SELECT * FROM employees;

INSERT INTO employees VALUES(1,"Anvesh",25000,"hyderabad");
INSERT INTO employees VALUES(2,"Surya",25000,"Kakinada");
INSERT INTO employees VALUES(3,"Ajay",35000,"Karimnagar");
INSERT INTO employees VALUES(4,"Upender",55000,"Kammam");

INSERT INTO employees(empId,ename,salary,city)
VALUES(4,"Nikhil",25000,"hyderabad");

DELETE FROM employees WHERE ename="Nikhil";

INSERT INTO employees(empId,ename,salary,city)
VALUES(5,"Nikhil",25000,"hyderabad");

INSERT INTO employees(empId,ename,salary,city)
VALUES(6,"Satish",105000,"Vishakapadnam"),
(7,"Prerana",123456,"Hyderabad");

SELECT * FROM employees;

UPDATE employees SET ename="Satti" WHERE ename="Satish";


UPDATE employees SET city="Vishakapatnam" WHERE empId= 6;


UPDATE employees SET city="Vishakapatnam" WHERE empId= 30;

INSERT INTO employees VALUES(8,"Upender",55000,"Kammam");

DELETE FROM employees WHERE empId=8;


TRUNCATE TABLE employees;

DROP TABLE employees;

DROP DATABASE IHUB;

```


---
# DQL / DRL
```sql

USE IHUB;

SHOW TABLES;

SELECT * FROM employees;

SELECT ename,salary FROM employees;

SELECT * FROM employees LIMIT 3;

SELECT * FROM employees LIMIT 2 OFFSET 2;

SELECT * FROM employees WHERE empId=3;

SELECT * FROM employees WHERE empId>=3;

SELECT * FROM employees WHERE empId IN (2,6,3);

SELECT * FROM employees WHERE empId NOT IN (2,6,3);

```


---

## Aggregate functions
- min , max, count , avg , sum

---

## Like 
- `_` for one charecter 
- `%` for 0 to more charecter
- `_a%` words which have 2nd letter a 

---


