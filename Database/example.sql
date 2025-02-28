-- Create the customer table
CREATE TABLE customer (
    CustomerID INT PRIMARY KEY,
    CustomerName VARCHAR(100),
    ContactName VARCHAR(100),
    Country VARCHAR(50)
);

-- Insert records into the customer table
INSERT INTO customer (CustomerID, CustomerName, ContactName, Country)
VALUES
    (1, 'Alfreds Futterkiste', 'Maria Anders', 'Germany'),
    (2, 'Ana Trujillo Emparedados y helados', 'Ana Trujillo', 'Mexico'),
    (3, 'Antonio Moreno Taquería', 'Antonio Moreno', 'Mexico');


-- Create the orders table
CREATE TABLE orders (
    OrderID INT PRIMARY KEY,
    CustomerID INT,
    OrderDate DATE
);

-- Insert records into the orders table
INSERT INTO orders (OrderID, CustomerID, OrderDate)
VALUES
    (10308, 2, '1996-09-18'),
    (10309, 37, '1996-09-19'),
    (10310, 77, '1996-09-20');

SELECT * FROM customer;

SELECT * FROM orders;

SELECT *
FROM Orders
RIGHT JOIN Customer ON Orders.CustomerID=Customer.CustomerID
WHERE Customer.CustomerID IS NOT NULL;


SELECT Database();




SELECT * FROM customer WHERE CustomerID IN (SELECT CustomerID FROM orders);

DELETE FROM orders WHERE CustomerID NOT IN (SELECT CustomerID FROM customer);