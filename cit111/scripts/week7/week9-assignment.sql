Use art_gallery;

-- Query #1 - Return two images where the period is Impressionism
SELECT artfile
FROM artwork
WHERE period = 'Impressionism';

-- Query #2 - Return files where the subject is related to flowers
SELECT a.artfile
FROM artwork a
JOIN artwork_has_keyword ak
ON a.artwork_id=ak.artwork_id
JOIN keyword k
ON k.keyword_id=ak.keyword_id
WHERE k.keyword LIKE '%flower%';

-- Query #3 - List all the arists from the artist table, but only the related artwork from the artwork table
SELECT ar.fname, ar.lname, aw.title
FROM artist ar
LEFT JOIN artwork aw
ON aw.artist_id=ar.artist_id;


-- Query #4 - List all subscriptions with the magazine name, last name, first name, and sort alphabetically
Use magazine;

SELECT m.magazineName, ss.subscriberFirstName, ss.subscriberLastName
FROM subscription s
LEFT JOIN magazine m 
ON s.magazineKey=m.magazineKey
JOIN subscriber ss
ON s.subscriberKey=ss.subscriberKey
ORDER BY 1 ASC;

-- Query #5 - List all the magazines that samantha sanders subscribes to
SELECT m.magazineName
FROM subscription s 
LEFT JOIN magazine m 
ON s.magazineKey=m.magazineKey
JOIN subscriber ss
ON s.subscriberKey=ss.subscriberKey
WHERE s.subscriberKey = 3

-- Query #6 - List the first five employees from the customer service department. Order alphabetically
Use employees;

SELECT e.first_name, e.last_name, d.dept_name
FROM employees e
JOIN dept_emp de
ON e.emp_no=de.emp_no
JOIN departments d
ON de.dept_no=d.dept_no
WHERE d.dept_name = 'Customer Service'
ORDER BY e.last_name ASC
LIMIT 5;

-- Query #7 - Find out the current salary and department of Berni Genin. Can ORder by and limit
SELECT e.first_name, e.last_name, d.dept_name, s.salary, s.from_date
FROM employees e
JOIN dept_emp de
ON e.emp_no=de.emp_no
JOIN departments d 
ON de.dept_no=d.dept_no
JOIN salaries s
ON e.emp_no=s.emp_no
WHERE e.first_name = 'Berni'
AND e.last_name = 'Genin'
ORDER BY 5 DESC
LIMIT 1;