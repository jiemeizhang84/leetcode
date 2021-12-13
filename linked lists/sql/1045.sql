SELECT tmp.customer_id
FROM (
    SELECT c.customer_id, p.product_key
    FROM customer c
    INNER JOIN product p 
    ON c.product_key = p.product_key   
) tmp
GROUP BY tmp.customer_id
HAVING COUNT(DISTINCT tmp.product_key) = (SELECT COUNT(DISTINCT product_key)FROM product)