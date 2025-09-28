DROP SCHEMA IF EXISTS test;

create schema test;
use test;

create table customers (
customer_id INT PRIMARY KEY,
name varchar(50),
city varchar(50)
);

create table orders (
order_id INT PRIMARY KEY,
customer_id INT,
product varchar(50)
);

create table payments (
payment_id INT PRIMARY KEY,
order_id INT ,
amount decimal(10,2)
);


select customers.customer_id, customers.name, 
orders.order_id,
orders.product, orders.customer_id as customer,
payments.payment_id, payments.amount 
from customers  
inner join orders
on customers.customer_id = orders.customer_id
left join payments 
on orders.order_id = payments.order_id;