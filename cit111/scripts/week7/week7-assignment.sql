
--Start of Art Gallery Queries
Use art_gallery;

--Query 1
INSERT INTO artist (artist_id, fname, mname, lname, dob, dod, country, local_artist)
VALUES (9, 'Johannes', '', 'Vermeer', 1632, 1674, 'Netherlands', 'n');

--Query 2
SELECT *
FROM artist
ORDER BY lname;

--Query 3
UPDATE artist
SET dod = 1675
WHERE artist_id = 9;

--Query 4
DELETE FROM artist
WHERE artist_id = 9;


--Start of Bike Shop queries
Use bike;

--Query 5
SELECT first_name, last_name, phone
FROM customer
WHERE phone LIKE '(281)%';

--Query 6
SELECT product_name, list_price, list_price - 500 AS Discount_Price
FROM product
WHERE list_price >= 5000
ORDER BY Discount_Price DESC;

--Query 7
SELECT first_name, last_name, email
FROM staff
WHERE store_id != 1;

--Query 8
SELECT product_name, model_year, list_price
FROM product
WHERE product_name LIKE '%Spider%';

--Query 9
SELECT product_name, list_price
FROM product
WHERE list_price >= 500 AND list_price <= 550
ORDER BY list_price;

--Query 10
SELECT first_name, last_name, phone, street, city, state, zip_code
FROM customer
WHERE phone IS NOT NULL
AND (city LIKE '%ach%' OR city LIKE '%och%')
OR last_name = 'William'
LIMIT 5;