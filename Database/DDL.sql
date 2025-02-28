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
-- DROP TABLE table1, table2, ... ;


-- - rename database
CREATE DATABASE NewDataBase NAME_CONST;

RENAME oldDataBaseName.tableName TO newDataBaseName.TABLE_NAME;


RENAME TABLE tableName to newTableName;

-- using change we can also change the datatype of the coloum 
ALTER TABLE tableName CHANGE COLUMN oldColName newColName dataType;
-- or
-- ALTER TABLE tableName CHANGE oldColName newColName dataType;


ALTER TABLE tableName RENAME COLUMN oldColName TO newColName;



