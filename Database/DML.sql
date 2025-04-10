CREATE DATABASE IHUB;

CREATE DATABASE IF NOT EXISTS IHUB;

USE IHUB;



CREATE TABLE employees(
    empId INT,
    ename VARCHAR(30),
    salary INT,
    city VARCHAR(30)
);

DROP employees;

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



-- table, entity, relation 
-- coloums, fields, attributes
-- row, tuple, record
-- database, schema 