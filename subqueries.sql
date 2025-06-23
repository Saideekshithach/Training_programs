create database counselling;
use counselling;
CREATE TABLE students (
    student_id INT PRIMARY KEY,
    name VARCHAR(50),
    gender VARCHAR(10),
    ranking INT,
    category VARCHAR(10),
    branch VARCHAR(10),
    college VARCHAR(50)
);
INSERT INTO students VALUES
(1, 'Anjali', 'Female', 45, 'OC', 'CSE', 'JNTU'),
(2, 'Ravi', 'Male', 120, 'BC', 'ECE', 'OU'),
(3, 'Sneha', 'Female', 89, 'SC', 'CSE', 'JNTU'),
(4, 'Karan', 'Male', 55, 'OC', 'EEE', 'CBIT'),
(5, 'Divya', 'Female', 150, 'BC', 'IT', 'MGIT'),
(6, 'Ajay', 'Male', 35, 'OC', 'CSE', 'JNTU');
SELECT name, ranking FROM students
WHERE ranking < (
    SELECT AVG(ranking) FROM students
);
SELECT name, ranking
FROM students
WHERE ranking = (
    SELECT MIN(ranking) FROM students
);
SELECT name, branch
FROM students
WHERE branch = (
    SELECT branch FROM students WHERE student_id = 1
);
SELECT DISTINCT college
FROM students
WHERE college IN (
    SELECT college FROM students WHERE category = 'OC'
);
SELECT name, ranking
FROM students
WHERE ranking < ALL (
    SELECT ranking FROM students WHERE gender = 'Female'
);
select avg(ranking) from students;




