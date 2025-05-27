# -- Problem 2: Find customers who bought ALL products
-- ================================================

# -- SOLUTION : Using GROUP BY and HAVING 
```
SELECT customer_id
FROM Customer
GROUP BY customer_id
HAVING COUNT(DISTINCT product_key) = (
    SELECT COUNT(*)
    FROM Product
);
```