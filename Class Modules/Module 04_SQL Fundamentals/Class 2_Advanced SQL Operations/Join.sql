-- Create a new schema for family data
DROP SCHEMA IF EXISTS test;
CREATE SCHEMA test;
USE test;


CREATE TABLE customers (
    customer_id INT PRIMARY KEY,
    name VARCHAR(50),
    city VARCHAR(50)
);


CREATE TABLE orders (
    order_id INT PRIMARY KEY,
    customer_id INT,
    product VARCHAR(50)
);

CREATE TABLE payments (
    payment_id INT PRIMARY KEY,
    order_id INT,
    amount DECIMAL(10,2)
);

-- INNER JOIN customers and orders
SELECT c.customer_id, c.name, o.order_id, o.product
FROM customers c
INNER JOIN orders o ON c.customer_id = o.customer_id;


SELECT c.customer_id, c.name, o.order_id, o.product
FROM customers c
LEFT JOIN orders o ON c.customer_id = o.customer_id;


SELECT o.order_id, o.product, c.customer_id, c.name
FROM customers c
RIGHT JOIN orders o ON o.customer_id = c.customer_id;

SELECT c.customer_id, c.name, o.order_id, o.product
FROM customers c
LEFT JOIN orders o ON c.customer_id = o.customer_id

UNION

SELECT c.customer_id, c.name, o.order_id, o.product
FROM customers c
RIGHT JOIN orders o ON c.customer_id = o.customer_id;