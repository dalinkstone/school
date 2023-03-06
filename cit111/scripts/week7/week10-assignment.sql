Use bike;

-- Query #1 - Get the average quantity that we have in all our bike stocks
SELECT ROUND(AVG(quantity), 0) AS 'Stock Average'
FROM stock;

-- Query #2 - Show each bike that needs to be reordered
SELECT product_name
FROM stock s
JOIN product p 
ON s.product_id=p.product_id
GROUP BY 1
HAVING MIN(s.quantity) = 0;

-- Query #3 - How many employees do we have?
Use employees;

SELECT COUNT(*)
FROM employees;

SELECT d.dept_name, FORMAT(AVG(s.salary), 2)
FROM salaries s
JOIN employees e
ON s.emp_no=e.emp_no
JOIN dept_emp de 
ON e.emp_no=de.emp_no
JOIN departments d
ON de.dept_no=d.dept_no
GROUP BY 1
HAVING AVG(s.salary) < 60000;

-- Query #6 - Find out how many females work in each department
SELECT d.dept_name, COUNT(e.gender)
FROM employees e
JOIN dept_emp de
ON e.emp_no=de.emp_no 
JOIN departments d
ON de.dept_no=d.dept_no
WHERE e.gender = 'F'
GROUP BY 1;
