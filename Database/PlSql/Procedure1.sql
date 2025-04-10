USE IHUB;

SHOW TABLES;

SELECT * FROM employees;





-- to execute muliple quaries we use procedures 
-- to store sequence of quearies we use procedure 

-- get all employees
CREATE PROCEDURE getAllEmp()
BEGIN
    SELECT * FROM employees;
END

CALL getAllEmp();



SELECT * FROM customer;



-- running multiple quaries
CREATE PROCEDURE getTwoTable()
BEGIN
    SELECT * FROM employees;
    SELECT * FROM customer;
END


CALL getTwoTable();



-- using parameters
CREATE PROCEDURE getSalGreaterThan(
    salary INT
)
BEGIN
    -- SELECT * FROM employees WHERE employees.salary >= salary
    -- SELECT * FROM employees as e WHERE e.salary >= salary
    SELECT * FROM employees e WHERE e.salary >= salary;
END


CALL getSalGreaterThan(35000);



DESC employees;



DROP PROCEDURE getSalCity;

DROP PROCEDURE IF EXISTS getSalCity;


CREATE PROCEDURE getSalCity(
    salary INT,
    city VARCHAR(30)
)
BEGIN
    SELECT * FROM employees as e WHERE e.salary >= salary AND e.city = city; 
END


CALL getSalCity(10000,"Hyderabad");

CALL getSalCity(20000,"Kakinada");




CREATE PROCEDURE getRecordById(
    empId INT
)
BEGIN
    SELECT * FROM employees as e WHERE e.empId = empId; 
END


CALL getRecordById(7);




CREATE PROCEDURE getEmp(
    empId INT
)
BEGIN
    IF empId IS NULL THEN
        SELECT * FROM employees;
    ELSE
        SELECT * FROM employees as e WHERE e.empId = empId;
    END IF;
END


CALL getEmp(7);

CALL getEmp(NULL);




CREATE PROCEDURE sumSal(
    OUT sal INT
)
BEGIN
    SELECT SUM(salary) INTO sal FROM employees;
END

CALL sumSal(@s);
SELECT @s;


set @sumSal = 0;
SELECT SUM(salary) INTO @sumSal FROM employees;

SELECT @sumSal;