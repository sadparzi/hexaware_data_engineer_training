CREATE DATABASE training_sql_db;
USE training_sql_db;

CREATE TABLE books
(
book_id INT PRIMARY KEY,
book_title VARCHAR(100),
category VARCHAR(50),
author VARCHAR(50),
price DECIMAL(10,2),
stock INT,
published_year INT
);

INSERT INTO books VALUES
(1, 'Python Basics', 'Programming', 'Ravi Kumar', 550, 30, 2021),
(2, 'Advanced SQL', 'Database', 'Priya Sharma', 750, 15, 2020),
(3, 'Data Engineering Guide', 'Data', 'Amit Verma', 1200, 10, 2023),
(4, 'Machine Learning Start', 'AI', 'Neha Reddy', 950, 8, 2022),
(5, 'Excel for Business', 'Business', 'Kiran Rao', 400, 50, 2019),
(6, 'Power BI Reports', 'Data', 'Sneha Patel', 850, 12, 2021),
(7, 'Java Fundamentals', 'Programming', 'Arjun Mehta', 600, 20, 2018),
(8, 'Cloud Basics', 'Cloud', 'Rahul Nair', 700, 18, 2022),
(9, 'SQL Interview Prep', 'Database', 'Farhan Ali', 500, 25, 2024),
(10, 'AI for Beginners', 'AI', 'Meera Singh', 650, 5, 2023);

-- exercise 1
SELECT * FROM books;

-- exercise 2
SELECT book_title, category, price 
FROM books;

-- exercise 3
SELECT DISTINCT category 
FROM books;

-- exercise 4
SELECT * 
FROM books 
WHERE category = 'Programming';

-- exercise 5
SELECT * 
FROM books 
WHERE price > 700;

-- exercise 6
SELECT * 
FROM books
WHERE stock < 15;

-- exercise 7
SELECT * 
FROM books 
WHERE category in 
('Programming','Database','AI');

-- exercise 8 
SELECT * 
FROM books 
WHERE price BETWEEN 500 AND 900;

-- exercise 9
SELECT * 
FROM books 
WHERE book_title like '%SQL%';

-- exercise 10
SELECT * 
FROM books 
WHERE book_title like 'Data%';

-- exercise 11
SELECT * 
FROM books 
ORDER BY price desc;

-- exercise 12
SELECT * 
FROM books 
ORDER BY category ASC, price DESC; 

-- exercise 13
SELECT COUNT(*)
FROM books;

-- exercise 14
SELECT *
FROM books
WHERE price = (select max(price) from books);

-- exercise 15
SELECT *
FROM books
WHERE price = (select min(price) from books);

-- exercise 16
SELECT AVG(price)
FROM books;

-- exercise 17
SELECT SUM(stock) AS TotalStock
FROM books;

-- exercise 18
SELECT category, COUNT(*) AS NumberOfBooks
FROM books
GROUP BY category;

-- exercise 19
SELECT category, AVG(price) AS AveragePrice
FROM books
GROUP BY category;

-- exercise 20
SELECT category, SUM(stock) AS TotalStock
FROM books
GROUP BY category;

-- exercise 21
SELECT category, COUNT(*) AS NumberOfBooks
FROM books
GROUP BY category
HAVING COUNT(*) > 1;

-- exercise 22
SELECT category, AVG(price) AS AveragePrice
FROM books
GROUP BY category
HAVING AVG(price) > 700;

CREATE TABLE departments
(
department_id INT PRIMARY KEY,
department_name VARCHAR(50),
location VARCHAR(50)
);

CREATE TABLE employees
(
employee_id INT PRIMARY KEY,
employee_name VARCHAR(50),
department_id INT,
salary DECIMAL(10,2),
city VARCHAR(50),
manager_id INT
);

INSERT INTO departments VALUES
(10, 'IT', 'Hyderabad'),
(20, 'HR', 'Bangalore'),
(30, 'Finance', 'Mumbai'),
(40, 'Sales', 'Delhi'),
(50, 'Marketing', NULL);

INSERT INTO employees VALUES
(101, 'Rahul Sharma', 10, 75000, 'Hyderabad', 201),
(102, 'Priya Reddy', 10, 85000, 'Bangalore', 201),
(103, 'Amit Kumar', 20, 55000, NULL, 202),
(104, 'Sneha Patel', 30, 65000, 'Mumbai', 203),
(105, 'Arjun Verma', NULL, 60000, 'Chennai', 204),
(106, 'Neha Singh', 60, 50000, 'Delhi', NULL),
(107, 'Farhan Ali', 40, NULL, 'Hyderabad', 205),
(108, 'Meera Nair', 10, 90000, 'Pune', 201);
