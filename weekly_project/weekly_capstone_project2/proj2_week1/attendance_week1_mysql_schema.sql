-- ============================================================
-- EMPLOYEE ATTENDANCE & PRODUCTIVITY TRACKER - WEEK 1
-- MySQL Schema, CRUD Operations, Stored Procedure
-- ============================================================

CREATE DATABASE IF NOT EXISTS attendance_tracker_db;
USE attendance_tracker_db;

-- ============================================================
-- SCHEMA: Tables
-- ============================================================

DROP TABLE IF EXISTS tasks;
DROP TABLE IF EXISTS attendance;
DROP TABLE IF EXISTS employees;

CREATE TABLE employees (
    employee_id INT PRIMARY KEY AUTO_INCREMENT,
    employee_name VARCHAR(100) NOT NULL,
    department VARCHAR(50) NOT NULL,
    role VARCHAR(50),
    hire_date DATE
);

CREATE TABLE attendance (
    attendance_id INT PRIMARY KEY AUTO_INCREMENT,
    employee_id INT,
    work_date DATE NOT NULL,
    clock_in TIME,
    clock_out TIME,
    status VARCHAR(20) DEFAULT 'Present',
    FOREIGN KEY (employee_id) REFERENCES employees(employee_id)
);

CREATE TABLE tasks (
    task_id INT PRIMARY KEY AUTO_INCREMENT,
    employee_id INT,
    task_date DATE NOT NULL,
    tasks_completed INT DEFAULT 0,
    tasks_assigned INT DEFAULT 0,
    FOREIGN KEY (employee_id) REFERENCES employees(employee_id)
);

-- ============================================================
-- INDEXES (fast querying by employee_id and department)
-- ============================================================

CREATE INDEX idx_attendance_employee ON attendance(employee_id);
CREATE INDEX idx_tasks_employee ON tasks(employee_id);
CREATE INDEX idx_employees_department ON employees(department);

-- ============================================================
-- CRUD: INSERT (Create)
-- ============================================================

INSERT INTO employees (employee_name, department, role, hire_date) VALUES
('Rahul Sharma', 'Engineering', 'Developer', '2021-02-01'),
('Priya Reddy', 'Engineering', 'Senior Developer', '2019-06-15'),
('Amit Kumar', 'Sales', 'Sales Executive', '2020-09-10'),
('Sneha Patel', 'HR', 'HR Manager', '2018-03-20'),
('Farhan Ali', 'Sales', 'Sales Manager', '2017-11-05'),
('Neha Singh', 'Marketing', 'Marketing Associate', '2022-01-12'),
('Arjun Verma', 'Engineering', 'QA Engineer', '2021-07-18'),
('Meera Nair', 'Marketing', 'Content Strategist', '2020-05-25');

INSERT INTO attendance (employee_id, work_date, clock_in, clock_out, status) VALUES
(1, '2026-06-01', '09:05:00', '18:10:00', 'Present'),
(2, '2026-06-01', '08:55:00', '18:00:00', 'Present'),
(3, '2026-06-01', '09:30:00', '17:45:00', 'Present'),
(4, '2026-06-01', '09:00:00', '18:00:00', 'Present'),
(5, '2026-06-01', NULL, NULL, 'Absent'),
(6, '2026-06-01', '09:15:00', '17:30:00', 'Present'),
(7, '2026-06-01', '09:50:00', '18:20:00', 'Present'),
(8, '2026-06-01', '09:00:00', '17:00:00', 'Present'),
(1, '2026-06-02', '09:00:00', '18:00:00', 'Present'),
(2, '2026-06-02', '09:10:00', '18:05:00', 'Present'),
(3, '2026-06-02', NULL, NULL, 'Absent'),
(4, '2026-06-02', '08:50:00', '17:55:00', 'Present'),
(5, '2026-06-02', '10:00:00', '18:30:00', 'Present'),
(6, '2026-06-02', '09:05:00', '17:40:00', 'Present'),
(7, '2026-06-02', '09:00:00', '18:00:00', 'Present'),
(8, '2026-06-02', '09:20:00', '17:50:00', 'Present');

INSERT INTO tasks (employee_id, task_date, tasks_completed, tasks_assigned) VALUES
(1, '2026-06-01', 5, 6),
(2, '2026-06-01', 8, 8),
(3, '2026-06-01', 3, 5),
(4, '2026-06-01', 4, 4),
(5, '2026-06-01', 0, 3),
(6, '2026-06-01', 6, 7),
(7, '2026-06-01', 5, 5),
(8, '2026-06-01', 4, 6),
(1, '2026-06-02', 6, 6),
(2, '2026-06-02', 7, 8),
(3, '2026-06-02', 0, 4),
(4, '2026-06-02', 5, 5),
(5, '2026-06-02', 2, 4),
(6, '2026-06-02', 5, 6),
(7, '2026-06-02', 6, 6),
(8, '2026-06-02', 3, 5);

-- ============================================================
-- CRUD: READ
-- ============================================================

SELECT * FROM employees;
SELECT * FROM attendance;
SELECT * FROM tasks;

-- Read: employee attendance + task detail
SELECT
    e.employee_name,
    e.department,
    a.work_date,
    a.clock_in,
    a.clock_out,
    a.status,
    t.tasks_completed,
    t.tasks_assigned
FROM attendance a
JOIN employees e ON a.employee_id = e.employee_id
LEFT JOIN tasks t ON a.employee_id = t.employee_id AND a.work_date = t.task_date
ORDER BY a.work_date, e.employee_name;

-- ============================================================
-- CRUD: UPDATE (e.g., clock-out correction)
-- ============================================================

UPDATE attendance
SET clock_out = '18:15:00'
WHERE attendance_id = 1;

UPDATE tasks
SET tasks_completed = 7
WHERE task_id = 1;

-- ============================================================
-- CRUD: DELETE
-- ============================================================

DELETE FROM attendance
WHERE attendance_id = 16;

-- ============================================================
-- STORED PROCEDURE: Total Working Hours per Employee
-- ============================================================

DELIMITER $$

CREATE PROCEDURE GetTotalWorkingHours(
    IN p_employee_id INT
)
BEGIN
    SELECT
        e.employee_name,
        e.department,
        COUNT(a.attendance_id) AS days_present,
        ROUND(SUM(TIMESTAMPDIFF(MINUTE, a.clock_in, a.clock_out)) / 60.0, 2) AS total_working_hours,
        ROUND(AVG(TIMESTAMPDIFF(MINUTE, a.clock_in, a.clock_out)) / 60.0, 2) AS avg_hours_per_day
    FROM attendance a
    JOIN employees e ON a.employee_id = e.employee_id
    WHERE a.employee_id = p_employee_id
      AND a.status = 'Present'
    GROUP BY e.employee_name, e.department;
END$$

DELIMITER ;

-- Example calls:
CALL GetTotalWorkingHours(1);
CALL GetTotalWorkingHours(2);
