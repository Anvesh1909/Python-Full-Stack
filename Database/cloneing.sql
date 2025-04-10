
USE ihub;

SHOW TABLES;

SELECT * FROM employees;

CREATE TABLE emp_simple_copy SELECT * FROM employees;

DROP TABLE emp_simple_copy;

SELECT * FROM emp_simple_copy;


DESC employees;

ALTER Table employees ADD CONSTRAINT pk_emp PRIMARY KEY(empId); 


DESC emp_simple_copy;


CREATE TABLE emp_shallow_copy LIKE employees;

SELECT * FROM emp_shallow_copy;

DESC emp_shallow_copy;



CREATE TABLE emp_deep_copy LIKE employees;
DESC emp_deep_copy;

INSERT INTO emp_deep_copy SELECT * FROM employees;

SELECT * FROM emp_deep_copy;

insert into employees(empid,ename,salary,city) VALUES(9,"parida",25000,"hyderabad")

CREATE table employee_shallow like employees;
CREATE Table simple_smp select *from employees;
CREATE table deep_emp like employees;
INSERT into deep_emp SELECT * from employees;
desc employee_shallow;
desc simple_smp;
SELECT * from employee_shallow;
SELECT * from simple_smp;


