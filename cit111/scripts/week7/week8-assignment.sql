USE magazine;

-- Query #1 - Take 3% Off that magazine price and round to two decimal places
SELECT magazineName, ROUND(magazinePrice - (magazinePrice * .03), 2) AS '3% Off'
FROM magazine;

-- Query #2 - How many years since subscription started from 2020-12-20
SELECT subscriptionKey, ROUND(DATEDIFF('2020-12-20', subscriptionStartDate) / 365, 0) AS 'Years since subscription'
FROM subscription;

-- Query #3 - How long a subscription will go for
SELECT subscriptionStartDate, subscriptionLength, DATE_FORMAT(DATE_ADD(subscriptionStartDate, INTERVAL subscriptionLength MONTH), '%M %e, %Y') AS 'Subscription end'
FROM subscription;

Use bike;
-- Query #4 - Product Name without Year
SELECT SUBSTRING_INDEX(product_name, ' - ', 1) AS 'Product Name without Year'
FROM product
ORDER BY product_id
LIMIT 14;

-- Query #5 - 2019 model 3 equal payments
SELECT product_name, CONCAT('$', FORMAT(list_price / 3, 2, 'en_US'))
FROM product
WHERE product_name LIKE '%- 2019';
