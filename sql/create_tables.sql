CREATE TABLE orders (
id SERIAL PRIMARY KEY,
client_order_id VARCHAR(50),
symbol VARCHAR(20),
side VARCHAR(10),
quantity INTEGER,
price DECIMAL(10,2),
status VARCHAR(20)
);
