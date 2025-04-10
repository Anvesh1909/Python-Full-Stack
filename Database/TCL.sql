-- transaction ensure data integrity and consistency in multistep operations that need to be atomic
-- commit
-- rollback
-- savepoint
-- release savepoint
-- set transaction


/*

commit
permanently saves all changes made during a transation to the database
rollback
it reverts the changes made during the currunt transaction to the last committed state
savepoint
creates a named point within a transaction to which you can rollback later
SAVEPOINT savepointName;
relese savepoint
to remove the savepoint 
start transaction 
configures transaction characteristics such as isolation level

to use transaction you must first start one with the START TRANSACTION ot BEGIN statement

*/


SELECT * FROM employees;

DELETE FROM employees WHERE empId > 7;


-- transaction 1 
START TRANSACTION;
INSERT INTO employees VALUES(10,"emp10",1234,"hyd");
UPDATE employees SET salary=25000 WHERE salary IS NULL;
ROLLBACK;



-- t2
START TRANSACTION;
INSERT INTO employees VALUES(10,"emp10",1234,"hyd");
UPDATE employees SET salary=25000 WHERE salary IS NULL;

COMMIT;

ROLLBACK;







SELECT * FROM employees;

DELETE FROM employees WHERE empId = 10;

-- t3
START TRANSACTION;

SAVEPOINT sp0;

INSERT INTO employees VALUES(10,"emp10",1234,"hyd");
-- UPDATE employees SET salary=25000 WHERE salary IS NULL;


SAVEPOINT sp1;


INSERT INTO employees VALUES(10,"emp10",1234,"hyd");
-- UPDATE employees SET salary=25000 WHERE salary IS NULL;


SAVEPOINT sp2;


ROLLBACK TO sp2;

ROLLBACK TO sp1;

ROLLBACK TO sp0;




ROLLBACK;

COMMIT;




