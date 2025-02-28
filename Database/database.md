## Database
- data is a raw facts 
- if it is organised this raw facts data into fields it is called information 
- Database is used to store data permenently and use it in future 
- file storage is not secure 
- database have authentication to make the database secure 
---
## SQL
- SQL stands for structure quary language
---
# databases
- Mysql, MongoDB, Oracle, Postgre Sql, MySQL Server, Casendra DB, Redis etc.
- it is an organised collection of data so that it can be easily accessed 
- to manage these database DBMS is used
- there are two types of DBMS
1. Relational DBMS (Mysql, Oracle etc...)
    - data is stored in table format and provided relation between the tables (rows,coloums)
    - it stores structured data
2. Non-Relational DBMS (MongoDB, Redis etc...)
    - data is stored in key:value pairs inside the curly braces.
    - it stores unstructred data
    ```json
    {
        "RollNo" : 1,
        "Class" : "5th",
        "Name" : "Srinivas" 
    }
    ```
- using sql quaries we can request the database and database will give responce

---
## RDBMS
- if we are providing relations between the tables it is called as RDBMS.
- by providing the relationship we can eliminate `Redundent`(duplicate) data.

- emp table without relations

| Eno | Name | deptid | deptName |
| -------- | ------- | --------- | --------- |
| 1 | name1 |  1 | HR |
| 2 | name2 |  1 | HR |
| 3 | name3 |  2 | Accounts |

- emp table with relations

| Eno | Name | deptid |
| -------- | ------- | ------- |
| 1 | name1 |  1 |
| 2 | name2 |  1 |
| 3 | name3 |  2 |

- dept table with relations

| deptid | deptName |
| ------- | --------- |
|  1 | HR |
|  1 | HR |
|  2 | Accounts |


---
# Mysql
- RDBMS, Open-Source, Free, 
- Deals with small and large applications
- fast, reliable, Scalable and easy to use
- Cross-platform 
- first released in 1995 by sun micro system 
- developed, distributed, and supported by oracle corporation
- usecases :- Facebook, Twitter. Airbus, booking.com. Uber, Github. Youtube etc...
---
## Database Table
- A table is a collection of related data enties and it consists of coloums and rows
- A coloum holds specific infomation of same datatype
---





# commands in mysql
- SELECT,  UPDATE, DELETE, INSERT INTO, CREATE DATABASE, ALTER DATABASE, CREATE TABLE, DROP etc...


---
