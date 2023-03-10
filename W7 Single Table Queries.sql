#W07 Assignment: Single Table Queries
#Luis Mendoza

# 1 Adding a new artist
USE art_gallery;

SELECT * FROM artist;
INSERT INTO artist VALUES
	(8, 'Johannes', NULL, 'Vermeer', 1632, 1674, 'Netherlands', 'n');

# 2 Alphabetically by the last name
SELECT * FROM artist
ORDER BY lname;

# 3 Update date of death
UPDATE artist
SET dod = 1675
WHERE artist_id = 8;

# 4 Delete Vermeer as an artist
DELETE FROM artist
WHERE artist_id = 8;

# 5 Text customer Houston, TX
USE bike;

SELECT first_name, last_name, phone FROM customer
WHERE city = 'Houston 'AND state = 'TX';

# 6 sell more high-end bikes
SELECT product_name, list_price, list_price - 500 AS 'Discount Price' FROM product
WHERE list_price > 5000
ORDER BY list_price DESC;

# 7 Announcement to all stores
SELECT first_name, last_name, email FROM staff
WHERE store_id <> 1;

# 8 Spider in the name
SELECT product_name, model_year, list_price FROM product
WHERE product_name LIKE '%spider%';

# 9 all bikes names prices between $500–$550
SELECT product_name, list_price FROM product
WHERE list_price BETWEEN 500 AND 550
ORDER BY list_price;

# 10 List of customers with phone, with ach or och, and with last name William
SELECT first_name, last_name, phone, street, city, state, zip_code FROM customer
WHERE phone IS NOT NULL AND city REGEXP 'ach|och' OR last_name = 'William'
LIMIT 5;






