SHOW DATABASES;

CREATE DATABASE Internship_supermarket;

USE Internship_supermarket;

SHOW TABLES;

CREATE TABLE products(
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(30) UNIQUE NOT NULL,
    quantity INT DEFAULT 1,
    price FLOAT,
    CHECK(quantity>=0)
)

DESC products;



INSERT INTO products(name,price) VALUES('Apple',100.00);
INSERT INTO products(name,price) VALUES('Banana',70.00);



SELECT * FROM products;

DROP TABLE products;