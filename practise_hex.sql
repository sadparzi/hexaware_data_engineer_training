CREATE DATABASE retail_db;
use retail_db;
create table customers(
	customer_id INT,
	customer_name VARCHAR (100),
    city VARCHAR (50)
);
INSERT INTO customers
VALUES
(1, 'Rahul', 'Hyderabad'),
(2, 'Priya', 'Bangalore'),
(3, 'Amit', 'Mumbai');

select * from customers;
set sql_safe_updates = 0;
update customers 
set city = 'Chennai'
where customer_id = 1;
delete from customers
where city = 'Bangalore';

CREATE TABLE products
(
    product_id INT PRIMARY KEY,
    product_name VARCHAR(100),
    category VARCHAR(50),
    price DECIMAL(10,2),
    stock_quantity INT,
    supplier_city VARCHAR(50)
);

insert into products values (1,'Laptop','Electronics',55000,10,'Hyderabad');
update products set price = 60000 where product_id = 1;
delete from products where product_id = 1;
select * from products;
INSERT INTO products VALUES
(1, 'Laptop', 'Electronics', 55000, 10, 'Hyderabad'),
(2, 'Mobile', 'Electronics', 25000, 25, 'Bangalore'),
(3, 'Printer', 'Electronics', 18000, 8, 'Pune'),
(4, 'Office Chair', 'Furniture', 7500, 15, 'Mumbai'),
(5, 'Desk', 'Furniture', 12000, 5, 'Chennai'),
(6, 'Notebook', 'Stationery', 80, 200, 'Hyderabad'),
(7, 'Pen', 'Stationery', 20, 500, 'Delhi'),
(8, 'Water Bottle', 'Accessories', 500, 50, 'Bangalore');
select product_name,price from products;
select distinct category from products;
select * from products where category = 'electronics';
SELECT *
FROM products
WHERE price > 10000;

SELECT *
FROM products
WHERE stock_quantity < 20;

SELECT *
FROM products
WHERE category = 'electronics'
and price > 10000;

SELECT *
FROM products
WHERE supplier_city = 'Hyderabad'
OR supplier_city = 'Bangalore';

SELECT *
FROM products
WHERE NOT category = 'electronics';

SELECT * 
FROM products 
WHERE supplier_city in ('Hyderabad','Delhi');

select * 
from products 
where price between 500 and 20000;

select * 
from products 
where product_name like "P%";
select * 
from products 
where product_name like "%k";

select * 
from products 
where product_name like "%top%";

select product_name as Product,
price as ProductPrice from products;

select * from products
order by price; -- desc for descending

select count(*) from products;

select count(*) from products
where category = 'Electronics';

select sum(price) from products;

SELECT
    COUNT(*) AS TotalProducts,
    SUM(price) AS TotalPrice,
    AVG(price) AS AveragePrice,
    MAX(price) AS HighestPrice,
    MIN(price) AS LowestPrice
FROM products;

select category,count(*) as ProductCount from products group by category;

select category,sum(price) as ProductCount from products group by category;

CREATE TABLE customers
(
    customer_id INT PRIMARY KEY,
    customer_name VARCHAR(50),
    city VARCHAR(50),
    phone VARCHAR(15)
);

CREATE TABLE orders
(
    order_id INT PRIMARY KEY,
    customer_id INT,
    product_name VARCHAR(50),
    order_amount DECIMAL(10,2),
    order_status VARCHAR(30)
);

INSERT INTO customers VALUES
(1, 'Rahul Sharma', 'Hyderabad', '9876543210'),
(2, 'Priya Reddy', 'Bangalore', '9876543211'),
(3, 'Amit Kumar', 'Mumbai', NULL),
(4, 'Sneha Patel', 'Chennai', '9876543213'),
(5, 'Arjun Verma', NULL, '9876543214'),
(6, 'Neha Singh', 'Delhi', '9876543215');

INSERT INTO orders VALUES
(101, 1, 'Laptop', 55000, 'Delivered'),
(102, 1, 'Mouse', 700, 'Delivered'),
(103, 2, 'Mobile', 25000, 'Shipped'),
(104, 3, 'Keyboard', NULL, 'Pending'),
(105, 7, 'Printer', 18000, 'Delivered'),
(106, NULL, 'Office Chair', 7500, 'Pending'),
(107, 4, NULL, 12000, 'Cancelled'),
(108, 8, 'Monitor', 15000, NULL);

SELECT
    c.customer_id,
    c.customer_name,
    c.city,
    o.order_id,
    o.product_name,
    o.order_amount,
    o.order_status
FROM customers c
INNER JOIN orders o
ON c.customer_id = o.customer_id;

SELECT
    c.customer_id,
    c.customer_name,
    c.city,
    o.order_id,
    o.product_name,
    o.order_amount,
    o.order_status
FROM customers c
LEFT JOIN orders o
ON c.customer_id = o.customer_id;

SELECT
    c.customer_id,
    c.customer_name,
    c.city,
    o.order_id,
    o.product_name,
    o.order_amount,
    o.order_status
FROM customers c
RIGHT JOIN orders o
ON c.customer_id = o.customer_id;

SELECT
    c.customer_id,
    c.customer_name,
    c.city,
    o.order_id,
    o.product_name,
    o.order_amount,
    o.order_status
FROM customers c
LEFT JOIN orders o
ON c.customer_id = o.customer_id
UNION
SELECT
    c.customer_id,
    c.customer_name,
    c.city,
    o.order_id,
    o.product_name,
    o.order_amount,
    o.order_status
FROM customers c
RIGHT JOIN orders o
ON c.customer_id = o.customer_id;

SELECT
    c.customer_id,
    c.customer_name
FROM customers c 
LEFT JOIN orders o 
on c.customer_id = o.customer_id
where o.order_id is NULL;



select * 
from customers 
where customer_id in 
(
select customer_id 
from orders
); 

SELECT customer_name
FROM customers
WHERE customer_id NOT IN
(
    SELECT customer_id
    FROM orders
    WHERE customer_id IS NOT NULL
);

select * 
from orders 
where order_amount > 
(
select avg(order_amount)
from orders
);

select * 
from orders 
where order_amount = 
(
select max(order_amount)
from orders
);