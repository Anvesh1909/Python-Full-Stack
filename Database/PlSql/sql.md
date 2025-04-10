Here are some examples of subqueries in SQL, along with the table schema and queries:

Example 1: Single-Row Subquery
Table Schema:


CREATE TABLE employees (
  employee_id INT PRIMARY KEY,
  name VARCHAR(255),
  salary DECIMAL(10, 2)
);

CREATE TABLE departments (
  department_id INT PRIMARY KEY,
  department_name VARCHAR(255)
);


Table Data:


INSERT INTO employees (employee_id, name, salary)
VALUES
  (1, 'John Doe', 50000.00),
  (2, 'Jane Smith', 60000.00),
  (3, 'Bob Johnson', 70000.00);

INSERT INTO departments (department_id, department_name)
VALUES
  (1, 'Sales'),
  (2, 'Marketing'),
  (3, 'IT');


Query:


SELECT *
FROM employees
WHERE salary > (SELECT AVG(salary) FROM employees);


Result:

| employee_id | name        | salary    |
|--------------|-------------|-----------|
| 3            | Bob Johnson | 70000.00  |

Example 2: Multiple-Row Subquery
Query:


SELECT *
FROM employees
WHERE department_id IN (SELECT department_id FROM departments WHERE department_name IN ('Sales', 'Marketing'));


Result:

| employee_id | name        | salary    | department_id |
|--------------|-------------|-----------|----------------|
| 1            | John Doe    | 50000.00  | 1               |
| 2            | Jane Smith  | 60000.00  | 2               |

Example 3: Correlated Subquery
Query:


SELECT *
FROM employees e
WHERE salary > (SELECT AVG(salary) FROM employees WHERE department_id = e.department_id);


Result:

| employee_id | name        | salary    | department_id |
|--------------|-------------|-----------|----------------|
| 3            | Bob Johnson | 70000.00  | 3               |

Example 4: Existence Subquery
Query:


SELECT *
FROM employees e
WHERE EXISTS (SELECT 1 FROM departments d WHERE d.department_id = e.department_id AND d.department_name = 'Sales');


Result:

| employee_id | name        | salary    | department_id |
|--------------|-------------|-----------|----------------|
| 1            | John Doe    | 50000.00  | 1               |

Example 5: Nested Subquery
Query:


SELECT *
FROM employees e
WHERE salary > (SELECT AVG(salary) FROM employees WHERE department_id IN (SELECT department_id FROM departments WHERE department_name IN ('Sales', 'Marketing')));


Result:

| employee_id | name        | salary    | department_id |
|--------------|-------------|-----------|----------------|
| 3            | Bob Johnson | 70000.00  | 3               |