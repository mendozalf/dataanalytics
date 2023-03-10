USE bike;

SELECT * FROM store;

SELECT CONCAT('The ' , store_name,' number is ', store_id) AS "Store's email"
FROM store;

SELECT LEFT(product_name, 15)
FROM product;

SELECT TRIM('  This is it  ');

SELECT RIGHT(product_name, 15)
FROM product;

SELECT UPPER(store_name) 
FROM store;

SELECT LOWER(store_name) 
FROM store;

# LOCATE(find, search, [start])

SELECT product_name, LOCATE('Girl', product_name, 1)
FROM product
WHERE LOCATE('Girl', product_name, 1) > 0;

# SUBSTRING(string, start, length) Return an string

SELECT product_name, SUBSTRING(product_name, LOCATE('Girl', product_name, 1), 6)
FROM product;

USE bike;


SELECT ROUND(list_price, 1)
FROM product;

SELECT CEILING(12.2);

SELECT FLOOR(12.9);

SELECT CONCAT('$', FORMAT(list_price, 2, 'en_US'))
FROM product;

SELECT order_date, YEAR(order_date)
FROM cust_order;

SELECT order_date, MONTH(order_date)
FROM cust_order;

SELECT order_date, DAY(order_date)
FROM cust_order;

SELECT HOUR(NOW());

SELECT YEAR(NOW());

SELECT NOW();

SELECT DATEDIFF(shipped_date, order_date)
FROM cust_order;

SELECT DATEDIFF(NOW(), order_date)/365
FROM cust_order;

SELECT DATEDIFF(order_date, shipped_date)
FROM cust_order;

SELECT order_date, DATE_ADD(order_date, INTERVAL 9 MONTH)
FROM cust_order;

SELECT DATE_FORMAT(order_date, '%M the %D %Y')
FROM cust_order;





