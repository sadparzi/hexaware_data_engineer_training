CREATE DATABASE retail_capstone_db;
USE retail_capstone_db;

CREATE TABLE customers
(
customer_id INT PRIMARY KEY,
customer_name VARCHAR(100),
city VARCHAR(50),
state VARCHAR(50),
gender VARCHAR(10),
membership_type VARCHAR(30)
);

CREATE TABLE products
(
product_id INT PRIMARY KEY,
product_name VARCHAR(100),
category VARCHAR(50),
price DECIMAL(10,2)
);

CREATE TABLE orders
(
order_id INT PRIMARY KEY,
customer_id INT,
order_date DATE,
order_status VARCHAR(30)
);

CREATE TABLE order_items
(
item_id INT PRIMARY KEY,
order_id INT,
product_id INT,
quantity INT
);

CREATE TABLE payments
(
payment_id INT PRIMARY KEY,
order_id INT,
payment_mode VARCHAR(30),
payment_status VARCHAR(30),
amount DECIMAL(10,2)
);

CREATE TABLE deliveries
(
delivery_id INT PRIMARY KEY,
order_id INT,
delivery_partner VARCHAR(50),
delivery_status VARCHAR(30),
delivery_city VARCHAR(50)
);

INSERT INTO customers VALUES
(1,'Rahul Sharma','Hyderabad','Telangana','Male','Gold'),
(2,'Priya Reddy','Hyderabad','Telangana','Female','Silver'),
(3,'Amit Kumar','Bangalore','Karnataka','Male','Gold'),
(4,'Sneha Patel','Mumbai','Maharashtra','Female','Bronze'),
(5,'Arjun Verma','Delhi','Delhi','Male','Silver'),
(6,'Meera Singh','Chennai','Tamil Nadu','Female','Gold'),
(7,'Farhan Ali','Pune','Maharashtra','Male','Bronze'),
(8,'Divya Nair','Kochi','Kerala','Female','Silver'),
(9,'Kiran Rao','Hyderabad','Telangana','Male','Gold'),
(10,'Neha Gupta','Bangalore','Karnataka','Female','Silver');

INSERT INTO products VALUES
(101,'iPhone 15','Electronics',75000),
(102,'Samsung TV','Electronics',45000),
(103,'Laptop Bag','Fashion',1500),
(104,'Running Shoes','Fashion',3500),
(105,'Bluetooth Speaker','Electronics',2500),
(106,'Office Chair','Furniture',5000),
(107,'Study Table','Furniture',7000),
(108,'Smart Watch','Electronics',6000),
(109,'T-Shirt','Fashion',800),
(110,'Headphones','Electronics',2000);

INSERT INTO orders VALUES
(1001,1,'2026-01-05','Delivered'),
(1002,2,'2026-01-08','Delivered'),
(1003,3,'2026-01-10','Pending'),
(1004,4,'2026-01-12','Cancelled'),
(1005,5,'2026-01-15','Delivered'),
(1006,6,'2026-01-18','Pending'),
(1007,1,'2026-01-20','Delivered'),
(1008,2,'2026-01-22','Delivered'),
(1009,7,'2026-01-25','Pending'),
(1010,8,'2026-01-27','Delivered'),
(1011,9,'2026-02-01','Cancelled'),
(1012,10,'2026-02-03','Delivered'),
(1013,3,'2026-02-05','Delivered'),
(1014,6,'2026-02-08','Pending'),
(1015,1,'2026-02-10','Delivered');

INSERT INTO order_items VALUES
(1,1001,101,1),
(2,1001,103,2),
(3,1002,104,1),
(4,1002,105,1),
(5,1003,108,1),
(6,1004,109,3),
(7,1005,102,1),
(8,1005,110,2),
(9,1006,103,1),
(10,1007,101,1),
(11,1007,110,1),
(12,1008,104,2),
(13,1009,105,3),
(14,1010,106,1),
(15,1011,109,2),
(16,1012,108,1),
(17,1013,102,1),
(18,1013,103,2),
(19,1014,107,1),
(20,1015,101,1);

INSERT INTO payments VALUES
(201,1001,'UPI','Success',78000),
(202,1002,'Card','Success',6000),
(203,1003,'UPI','Pending',6000),
(204,1004,'Card','Success',2400),
(205,1005,'Net Banking','Success',49000),
(206,1006,'UPI','Pending',1500),
(207,1007,'Card','Success',77000),
(208,1008,'UPI','Success',7000),
(209,1009,'Cash','Pending',7500),
(210,1010,'UPI','Success',5000),
(211,1011,'Card','Failed',1600),
(212,1012,'UPI','Success',6000),
(213,1013,'Net Banking','Success',48000),
(214,1014,'UPI','Pending',7000),
(215,1015,'Card','Success',75000);

INSERT INTO deliveries VALUES
(301,1001,'Delhivery','Delivered','Hyderabad'),
(302,1002,'BlueDart','Delivered','Hyderabad'),
(303,1003,'Ekart','Pending','Bangalore'),
(304,1004,'Delhivery','Cancelled','Mumbai'),
(305,1005,'BlueDart','Delivered','Delhi'),
(306,1006,'Ekart','Pending','Chennai'),
(307,1007,'Delhivery','Delivered','Hyderabad'),
(308,1008,'BlueDart','Delivered','Hyderabad'),
(309,1009,'Ekart','Pending','Pune'),
(310,1010,'Delhivery','Delivered','Kochi'),
(311,1011,'BlueDart','Cancelled','Hyderabad'),
(312,1012,'Ekart','Delivered','Bangalore'),
(313,1013,'Delhivery','Delivered','Bangalore'),
(314,1014,'BlueDart','Pending','Chennai'),
(315,1015,'Ekart','Delivered','Hyderabad');

-- create and insert into tables done'

-- query 1 
SELECT *
FROM customers;

-- query 2
SELECT
    customer_name,
    city,
    membership_type
FROM customers;

-- query 3
SELECT *
FROM products
ORDER BY price DESC;

-- query 4
SELECT *
FROM customers
WHERE city = 'Hyderabad';

-- query 5
SELECT *
FROM customers
WHERE membership_type = 'Gold';

-- query 6
SELECT *
FROM products
WHERE price BETWEEN 500 AND 5000;

-- query 7
SELECT *
FROM products
WHERE category IN ('Electronics', 'Fashion');

-- query 8
SELECT *
FROM orders
WHERE order_date > '2026-01-01';

-- query 9
SELECT *
FROM payments
WHERE payment_mode = 'UPI';

-- query 10
SELECT *
FROM deliveries
WHERE delivery_status = 'Pending';

-- query 11
SELECT COUNT(*) AS TotalCustomers
FROM customers;

-- query 12
SELECT COUNT(*) AS TotalOrders
FROM orders;

-- query 13
SELECT COUNT(*) AS TotalProducts
FROM products;

-- query 14
SELECT SUM(amount) AS TotalRevenue
FROM payments
WHERE payment_status = 'Success';

-- query 15
SELECT AVG(amount) AS AveragePayment
FROM payments;

-- query 16
SELECT MAX(amount) AS HighestPayment
FROM payments;

-- query 17
SELECT MIN(amount) AS LowestPayment
FROM payments;

-- query 18
SELECT
    city,
    COUNT(*) AS CustomerCount
FROM customers
GROUP BY city;

-- query 19
SELECT
    category,
    COUNT(*) AS ProductCount
FROM products
GROUP BY category;

-- query 20
SELECT
    order_status,
    COUNT(*) AS OrderCount
FROM orders
GROUP BY order_status;

-- query 21
SELECT
    c.customer_name,
    o.order_id,
    o.order_date
FROM customers c
INNER JOIN orders o
ON c.customer_id = o.customer_id;

-- query 22
SELECT
    oi.order_id,
    p.product_name,
    oi.quantity,
    p.price
FROM order_items oi
INNER JOIN products p
ON oi.product_id = p.product_id;

-- query 23
SELECT
    c.customer_name,
    p.product_name,
    oi.quantity,
    o.order_date
FROM customers c
INNER JOIN orders o
ON c.customer_id = o.customer_id
INNER JOIN order_items oi
ON o.order_id = oi.order_id
INNER JOIN products p
ON oi.product_id = p.product_id;

-- query 24
SELECT
    o.order_id,
    p.payment_mode,
    p.payment_status,
    p.amount
FROM orders o
INNER JOIN payments p
ON o.order_id = p.order_id;

-- query 25
SELECT
    o.order_id,
    d.delivery_partner,
    d.delivery_status
FROM orders o
INNER JOIN deliveries d
ON o.order_id = d.order_id;

-- query 26
SELECT
    c.customer_name,
    c.city,
    o.order_id,
    o.order_date,
    p.product_name,
    p.category,
    oi.quantity,
    p.price,
    pay.payment_status,
    d.delivery_status
FROM customers c
INNER JOIN orders o
ON c.customer_id = o.customer_id
INNER JOIN order_items oi
ON o.order_id = oi.order_id
INNER JOIN products p
ON oi.product_id = p.product_id
INNER JOIN payments pay
ON o.order_id = pay.order_id
INNER JOIN deliveries d
ON o.order_id = d.order_id;

-- query 27
SELECT
    c.city,
    SUM(pay.amount) AS TotalRevenue
FROM customers c
INNER JOIN orders o
ON c.customer_id = o.customer_id
INNER JOIN payments pay
ON o.order_id = pay.order_id
WHERE pay.payment_status = 'Success'
GROUP BY c.city;

-- query 28
SELECT
    c.customer_name,
    SUM(pay.amount) AS TotalRevenue
FROM customers c
INNER JOIN orders o
ON c.customer_id = o.customer_id
INNER JOIN payments pay
ON o.order_id = pay.order_id
WHERE pay.payment_status = 'Success'
GROUP BY c.customer_name;

-- query 29
SELECT
    p.product_name,
    SUM(oi.quantity) AS TotalQuantitySold
FROM products p
INNER JOIN order_items oi
ON p.product_id = oi.product_id
GROUP BY p.product_name;

-- query 30
SELECT
    p.category,
    SUM(oi.quantity * p.price) AS Revenue
FROM products p
INNER JOIN order_items oi
ON p.product_id = oi.product_id
GROUP BY p.category;

-- query 31
SELECT
    c.customer_name,
    COUNT(o.order_id) AS NumberOfOrders
FROM customers c
INNER JOIN orders o
ON c.customer_id = o.customer_id
GROUP BY c.customer_name;

-- query 32
SELECT
    c.customer_name,
    COUNT(o.order_id) AS NumberOfOrders
FROM customers c
INNER JOIN orders o
ON c.customer_id = o.customer_id
GROUP BY c.customer_name
HAVING COUNT(o.order_id) > 1;

-- query 33
SELECT
    p.category,
    SUM(oi.quantity * p.price) AS Revenue
FROM products p
INNER JOIN order_items oi
ON p.product_id = oi.product_id
GROUP BY p.category
HAVING SUM(oi.quantity * p.price) > 10000;

-- query 34
SELECT
    city,
    COUNT(*) AS CustomerCount
FROM customers
GROUP BY city
HAVING COUNT(*) > 2;

-- query 35
SELECT
    p.product_name,
    SUM(oi.quantity) AS TotalSold
FROM products p
INNER JOIN order_items oi
ON p.product_id = oi.product_id
GROUP BY p.product_name
HAVING SUM(oi.quantity) > 3;

-- query 36
SELECT *
FROM customers
WHERE customer_id IN
(
    SELECT customer_id
    FROM orders
);

-- query 37
SELECT *
FROM customers
WHERE customer_id NOT IN
(
    SELECT customer_id
    FROM orders
);

-- query 38
SELECT *
FROM products
WHERE product_id NOT IN
(
    SELECT product_id
    FROM order_items
);

-- query 39
SELECT *
FROM payments
WHERE amount >
(
    SELECT AVG(amount)
    FROM payments
);

-- query 40
SELECT DISTINCT
    c.customer_id,
    c.customer_name
FROM customers c
INNER JOIN orders o
ON c.customer_id = o.customer_id
INNER JOIN payments p
ON o.order_id = p.order_id
WHERE p.amount =
(
    SELECT MAX(amount)
    FROM payments
);

-- query 41
SELECT *
FROM products
WHERE price >
(
    SELECT AVG(price)
    FROM products
);

-- query 42
SELECT *
FROM products
WHERE price >
(
    SELECT AVG(price)
    FROM products
);

-- query 43
SELECT *
FROM orders
WHERE order_id IN
(
    SELECT order_id
    FROM payments
    WHERE payment_status = 'Success'
);

-- query 44
SELECT *
FROM orders
WHERE order_id IN
(
    SELECT order_id
    FROM deliveries
    WHERE delivery_status <> 'Delivered'
);

-- query 45
SELECT
    c.customer_id,
    c.customer_name,
    SUM(p.amount) AS TotalSpending
FROM customers c
INNER JOIN orders o
ON c.customer_id = o.customer_id
INNER JOIN payments p
ON o.order_id = p.order_id
WHERE p.payment_status = 'Success'
GROUP BY c.customer_id, c.customer_name
HAVING SUM(p.amount) >
(
    SELECT AVG(CustomerTotal)
    FROM
    (
        SELECT SUM(p2.amount) AS CustomerTotal
        FROM customers c2
        INNER JOIN orders o2
        ON c2.customer_id = o2.customer_id
        INNER JOIN payments p2
        ON o2.order_id = p2.order_id
        WHERE p2.payment_status = 'Success'
        GROUP BY c2.customer_id
    ) AS AvgTable
);

-- query 46
SELECT o.*
FROM orders o
LEFT JOIN payments p
ON o.order_id = p.order_id
WHERE p.order_id IS NULL;

-- query 47
SELECT o.*
FROM orders o
LEFT JOIN deliveries d
ON o.order_id = d.order_id
WHERE d.order_id IS NULL;

-- query 48
SELECT *
FROM payments
WHERE amount IS NULL
OR amount = 0;

-- query 49
SELECT
    o.order_id,
    o.order_status,
    p.payment_status
FROM orders o
INNER JOIN payments p
ON o.order_id = p.order_id
WHERE o.order_status = 'Cancelled'
AND p.payment_status = 'Success';

-- query 50
SELECT
    o.order_id,
    d.delivery_status,
    p.payment_status
FROM orders o
INNER JOIN deliveries d
ON o.order_id = d.order_id
INNER JOIN payments p
ON o.order_id = p.order_id
WHERE d.delivery_status = 'Delivered'
AND p.payment_status = 'Failed';

-- query 51
SELECT oi.*
FROM order_items oi
LEFT JOIN products p
ON oi.product_id = p.product_id
WHERE p.product_id IS NULL;

-- query 52
SELECT o.*
FROM orders o
LEFT JOIN customers c
ON o.customer_id = c.customer_id
WHERE c.customer_id IS NULL;