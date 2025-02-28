USE IHUB;

SHOW TABLES;

SELECT * FROM employees;

SELECT ename,salary FROM employees;


-- limit clause
SELECT * FROM employees LIMIT 3;


-- limit clause with offset clause
SELECT * FROM employees LIMIT 20 OFFSET 2;


-- where clause
SELECT * FROM employees WHERE empId=3;


SELECT * FROM employees WHERE empId>=3;

SELECT * FROM employees WHERE empId IN (2,6,3);

SELECT * FROM employees WHERE empId NOT IN (2,6,3);


-- order by clause
SELECT * FROM employees ORDER BY ename;

SELECT * FROM employees ORDER BY salary;

SELECT * FROM employees ORDER BY salary ASC;

SELECT * FROM employees ORDER BY salary DESC;

SELECT * FROM employees ORDER BY city ASC, salary DESC;


SELECT city from employees;


-- distinct 
-- to display unique cities
SELECT DISTINCT city from employees;

SELECT DISTINCT city , salary FROM employees;

SELECT DISTINCT * from employees;


-- aggregate functions
SELECT MAX(salary) FROM employees;

SELECT MIN(salary) FROM employees;


SELECT COUNT(salary) FROM employees;

SELECT AVG(salary) FROM employees;


SELECT SUM(salary) FROM employees;


SELECT * FROM employees;

SELECT empid AS employee_Id , ename AS employee_name , salary AS employee_salary FROM employees;

-- not prefered
SELECT empid employee_Id , ename employee_name , salary employee_salary FROM employees;


-- between clause
SELECT * FROM employees;

SELECT * FROM employees WHERE salary BETWEEN 30000 AND 100000;

SELECT * FROM employees WHERE salary NOT BETWEEN 30000 AND 100000;


-- in clause
SELECT * FROM employees;


SELECT * FROM employees WHERE empid IN (1,3,5,7,9);

SELECT * FROM employees WHERE empid IN (2,4,6,8,10);

SELECT * FROM employees WHERE empid NOT IN (2,4,6,8,10);

SELECT * FROM employees WHERE city="Hyderabad" AND salary>100000;


SELECT * FROM employees WHERE city="Hyderabad" OR salary>100000;


-- relational operators
SELECT * FROM employees WHERE empid = 4;

SELECT * FROM employees WHERE empid != 4;

SELECT * FROM employees WHERE empid > 4;

SELECT * FROM employees WHERE empid >= 4;

SELECT * FROM employees WHERE empid < 4;

SELECT * FROM employees WHERE empid <= 4;



-- like operator

SELECT * FROM employees;


SELECT * FROM employees WHERE ename = "Anvesh";

-- ename starting with A
SELECT * FROM employees WHERE ename LIKE "A%";

SELECT * FROM employees WHERE ename LIKE "A%";

-- ending with H
SELECT * FROM employees WHERE ename LIKE "%h";

-- name containing e
SELECT * FROM employees WHERE ename LIKE "%e%";

-- under score represent single charecter 
-- % 0 or more charecters

-- secound letter is a 
SELECT * FROM employees WHERE ename LIKE "_a%";



-- third letter is a 
SELECT * FROM employees WHERE ename LIKE "__a%";



-- five letter name 
SELECT * FROM employees WHERE ename LIKE "_____";




SELECT * FROM employees;

UPDATE employees SET salary = 4000000 WHERE empId = 7;

SELECT * FROM employees;


INSERT INTO employees VALUES(8,"Hello",NULL,NULL);

SELECT * FROM employees WHERE salary=NULL;

SELECT * FROM employees WHERE salary IS NULL;

SELECT * FROM employees WHERE salary IS NOT NULL;


DELETE FROM employees WHERE empId = 8 LIMIT 2;



SELECT * FROM employees;

UPDATE employees SET salary = 4000000 WHERE empId = 8 LIMIT 1;


SELECT * FROM employees WHERE empId = (SELECT COUNT(empId) FROM employees);


INSERT INTO employees VALUES(9,"anvesh",NULL,NULL);

SELECT * FROM employees WHERE ename LIKE "a3%";


