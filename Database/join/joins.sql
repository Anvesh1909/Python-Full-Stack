USE ihub;

SELECT * FROM employees;


CREATE TABLE table_A(
    id INT PRIMARY KEY AUTO_INCREMENT,
    color VARCHAR(20)
);




CREATE TABLE table_B(
    id INT PRIMARY KEY AUTO_INCREMENT,
    color VARCHAR(20)
);




INSERT INTO table_a(color) VALUES("RED");
INSERT INTO table_a(color) VALUES("GREEN");
INSERT INTO table_a(color) VALUES("BLUE");
INSERT INTO table_a(color) VALUES("PURPLE");


SELECT * FROM table_a;

TRUNCATE TABLE table_a;




INSERT INTO table_b(color) VALUES("RED");
INSERT INTO table_b(color) VALUES("GREEN");
INSERT INTO table_b(color) VALUES("BROWN");
INSERT INTO table_b(color) VALUES("GRAY");


SELECT * FROM table_b;




-- inner join 
SELECT * FROM table_a INNER JOIN table_b ON table_a.color = table_b.color;


SELECT * FROM table_a LEFT JOIN table_b ON table_a.color = table_b.color;


SELECT * FROM table_a RIGHT JOIN table_b ON table_a.color = table_b.color;


SELECT * FROM table_a LEFT JOIN table_b ON table_a.color = table_b.color WHERE table_b.id IS NULL;


-- right outer join 
SELECT * FROM table_a RIGHT JOIN table_b ON table_a.color = table_b.color WHERE table_a.id IS NULL;




-- full join
SELECT * FROM table_a LEFT JOIN table_b ON table_a.color = table_b.color
UNION
SELECT * FROM table_a RIGHT JOIN table_b ON table_a.color = table_b.color;


