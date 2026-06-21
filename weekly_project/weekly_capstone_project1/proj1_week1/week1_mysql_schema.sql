-- ============================================================
-- RETAIL SALES PERFORMANCE DASHBOARD - WEEK 1
-- MySQL Schema, CRUD Operations, Stored Procedure
-- ============================================================

CREATE DATABASE IF NOT EXISTS retail_sales_db;
USE retail_sales_db;

-- ============================================================
-- SCHEMA: Tables
-- ============================================================

DROP TABLE IF EXISTS sales;
DROP TABLE IF EXISTS employees;
DROP TABLE IF EXISTS products;
DROP TABLE IF EXISTS stores;

CREATE TABLE stores (
    store_id INT PRIMARY KEY AUTO_INCREMENT,
    store_name VARCHAR(100) NOT NULL,
    region VARCHAR(50) NOT NULL,
    city VARCHAR(50) NOT NULL,
    opened_date DATE
);

CREATE TABLE products (
    product_id INT PRIMARY KEY AUTO_INCREMENT,
    product_name VARCHAR(100) NOT NULL,
    category VARCHAR(50) NOT NULL,
    price DECIMAL(10,2) NOT NULL,
    cost DECIMAL(10,2) NOT NULL
);

CREATE TABLE employees (
    employee_id INT PRIMARY KEY AUTO_INCREMENT,
    employee_name VARCHAR(100) NOT NULL,
    store_id INT,
    role VARCHAR(50),
    hire_date DATE,
    FOREIGN KEY (store_id) REFERENCES stores(store_id)
);

CREATE TABLE sales (
    sale_id INT PRIMARY KEY AUTO_INCREMENT,
    store_id INT,
    product_id INT,
    employee_id INT,
    quantity INT NOT NULL,
    sale_date DATE NOT NULL,
    discount_pct DECIMAL(5,2) DEFAULT 0,
    FOREIGN KEY (store_id) REFERENCES stores(store_id),
    FOREIGN KEY (product_id) REFERENCES products(product_id),
    FOREIGN KEY (employee_id) REFERENCES employees(employee_id)
);

-- ============================================================
-- INDEXES (search by product and region)
-- ============================================================

CREATE INDEX idx_sales_product ON sales(product_id);
CREATE INDEX idx_stores_region ON stores(region);

-- ============================================================
-- CRUD: INSERT (Create)
-- ============================================================

INSERT INTO stores (store_name, region, city, opened_date) VALUES
('Downtown Mart', 'South', 'Chennai', '2020-01-15'),
('City Center Store', 'South', 'Bangalore', '2019-06-10'),
('North Plaza', 'North', 'Delhi', '2021-03-22'),
('West End Outlet', 'West', 'Mumbai', '2018-11-05'),
('East Side Shop', 'East', 'Kolkata', '2022-07-18');

INSERT INTO products (product_name, category, price, cost) VALUES
('Wireless Mouse', 'Electronics', 599.00, 350.00),
('Bluetooth Speaker', 'Electronics', 1499.00, 900.00),
('Cotton T-Shirt', 'Apparel', 499.00, 200.00),
('Running Shoes', 'Footwear', 2999.00, 1800.00),
('Coffee Maker', 'Appliances', 3499.00, 2200.00),
('Yoga Mat', 'Fitness', 899.00, 450.00),
('Backpack', 'Accessories', 1299.00, 700.00),
('Desk Lamp', 'Home', 799.00, 400.00);

INSERT INTO employees (employee_name, store_id, role, hire_date) VALUES
('Rahul Sharma', 1, 'Manager', '2020-02-01'),
('Priya Reddy', 1, 'Sales Associate', '2021-05-10'),
('Amit Kumar', 2, 'Manager', '2019-07-01'),
('Sneha Patel', 3, 'Sales Associate', '2021-04-15'),
('Farhan Ali', 4, 'Manager', '2018-12-01'),
('Neha Singh', 5, 'Sales Associate', '2022-08-01');

INSERT INTO sales (store_id, product_id, employee_id, quantity, sale_date, discount_pct) VALUES
(1, 1, 2, 5, '2026-06-01', 5.00),
(1, 3, 2, 10, '2026-06-01', 0.00),
(2, 2, 3, 3, '2026-06-02', 10.00),
(2, 4, 3, 2, '2026-06-02', 0.00),
(3, 5, 4, 1, '2026-06-03', 15.00),
(3, 6, 4, 7, '2026-06-03', 0.00),
(4, 7, 5, 4, '2026-06-04', 5.00),
(4, 8, 5, 6, '2026-06-04', 0.00),
(5, 1, 6, 8, '2026-06-05', 0.00),
(5, 3, 6, 12, '2026-06-05', 20.00),
(1, 4, 2, 2, '2026-06-06', 0.00),
(2, 5, 3, 1, '2026-06-06', 10.00);

-- ============================================================
-- CRUD: READ
-- ============================================================

SELECT * FROM stores;
SELECT * FROM products;
SELECT * FROM employees;
SELECT * FROM sales;

-- Read with join: full sales detail
SELECT
    s.sale_id,
    st.store_name,
    p.product_name,
    e.employee_name,
    s.quantity,
    s.sale_date,
    s.discount_pct
FROM sales s
JOIN stores st ON s.store_id = st.store_id
JOIN products p ON s.product_id = p.product_id
JOIN employees e ON s.employee_id = e.employee_id;

-- ============================================================
-- CRUD: UPDATE
-- ============================================================

UPDATE products
SET price = 649.00
WHERE product_name = 'Wireless Mouse';

UPDATE sales
SET discount_pct = 10.00
WHERE sale_id = 1;

-- ============================================================
-- CRUD: DELETE
-- ============================================================

DELETE FROM sales
WHERE sale_id = 12;

-- ============================================================
-- STORED PROCEDURE: Calculate Daily Sales for a Store
-- ============================================================

DELIMITER $$

CREATE PROCEDURE GetDailySalesByStore(
    IN p_store_id INT,
    IN p_sale_date DATE
)
BEGIN
    SELECT
        st.store_name,
        s.sale_date,
        SUM(s.quantity) AS total_units_sold,
        SUM(s.quantity * p.price * (1 - s.discount_pct / 100)) AS total_revenue,
        SUM(s.quantity * p.cost) AS total_cost,
        SUM(s.quantity * p.price * (1 - s.discount_pct / 100)) - SUM(s.quantity * p.cost) AS total_profit
    FROM sales s
    JOIN stores st ON s.store_id = st.store_id
    JOIN products p ON s.product_id = p.product_id
    WHERE s.store_id = p_store_id
      AND s.sale_date = p_sale_date
    GROUP BY st.store_name, s.sale_date;
END$$

DELIMITER ;

-- Example call:
CALL GetDailySalesByStore(1, '2026-06-01');
CALL GetDailySalesByStore(2, '2026-06-02');
