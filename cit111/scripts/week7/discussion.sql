We need all the bikes product names that start with A-H and whose list price is more than $299.99 or exactly $299.99. Sort them by product name. We will need to inventory those bikes first during inventory.

USE bike;

SELECT *
FROM product
WHERE product_name REGEXP '^[A-H].*'
AND list_price <= 299.99
ORDER BY product_name