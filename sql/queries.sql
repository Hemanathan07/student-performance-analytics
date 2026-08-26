-- STUDENT PERFORMANCE ANALYTICS - SQL LAYER
-- Combines Phase 9 (Fundamentals) + Phase 10 (Advanced SQL)

-- 1. Create the core table
CREATE TABLE students (
    id INT PRIMARY KEY,
    name VARCHAR(100),
    department VARCHAR(50),
    python INT,
    maths INT,
    database_mark INT
);

-- 2. Insert sample data
INSERT INTO students VALUES
(1, 'Asha', 'CSE', 80, 78, 85),
(2, 'Bala', 'CSE', 72, 75, 70),
(3, 'Cathy', 'IT', 91, 95, 89),
(4, 'Dinesh', 'ECE', 65, 60, 68),
(5, 'Esha', 'IT', 88, 84, 90);

-- 3. Basic queries
SELECT * FROM students;

SELECT name, department, python
FROM students
WHERE python >= 80
ORDER BY python DESC;

SELECT department,
       COUNT(*) AS student_count,
       AVG(python) AS avg_python
FROM students
GROUP BY department;

-- 4. Advanced: ranking, performance levels, department join
SELECT
    name,
    department,
    ROUND((python + maths + database_mark) / 3.0, 2) AS average_mark
FROM students
ORDER BY average_mark DESC;

SELECT
    name,
    department,
    RANK() OVER (
        ORDER BY (python + maths + database_mark) DESC
    ) AS rank_no
FROM students;

SELECT
    name,
    CASE
        WHEN (python + maths + database_mark) / 3.0 >= 80 THEN 'HIGH'
        WHEN (python + maths + database_mark) / 3.0 >= 60 THEN 'MEDIUM'
        ELSE 'LOW'
    END AS performance_level
FROM students;

CREATE TABLE departments (
    department_code VARCHAR(10) PRIMARY KEY,
    department_name VARCHAR(100)
);

INSERT INTO departments VALUES
('CSE', 'Computer Science'),
('IT', 'Information Technology'),
('ECE', 'Electronics and Communication');

SELECT s.name, s.department, d.department_name
FROM students s
LEFT JOIN departments d
ON s.department = d.department_code;
