CREATE TABLE customers (
    customer_id VARCHAR PRIMARY KEY,
    customer_unique_id VARCHAR,
    customer_zip_code_prefix INT,
    customer_city VARCHAR,
    customer_state VARCHAR
);

CREATE TABLE orders (
    order_id VARCHAR PRIMARY KEY,
    customer_id VARCHAR REFERENCES customers(customer_id),
    order_status VARCHAR,
    order_purchase_timestamp TIMESTAMP,
    delivery_days INT,
    delivery_status VARCHAR
);

CREATE TABLE order_items (
    order_id VARCHAR,
    product_id VARCHAR,
    seller_id VARCHAR,
    price NUMERIC,
    freight_value NUMERIC
);

-- Continue for payments, products, sellers and reviews