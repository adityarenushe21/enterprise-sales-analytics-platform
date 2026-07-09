--Total Revenue


SELECT SUM(payment_value) AS total_revenue
FROM payments;


--Total Orders


SELECT COUNT(DISTINCT order_id)
FROM orders;
Top Product Categories
SELECT
    p.product_category_name_english,
    SUM(oi.price) AS revenue
FROM order_items oi
JOIN products p
ON oi.product_id = p.product_id
GROUP BY p.product_category_name_english
ORDER BY revenue DESC
LIMIT 10;


--Average Rating

SELECT AVG(review_score)
FROM reviews;


--Late Deliveries

SELECT delivery_status,
COUNT(*)
FROM orders
GROUP BY delivery_status;