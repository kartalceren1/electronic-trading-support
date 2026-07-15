CREATE TABLE orders (
id SERIAL PRIMARY KEY,
client_order_id VARCHAR(50),
symbol VARCHAR(20),
side VARCHAR(10),
quantity INTEGER,
price DECIMAL(10,2),
status VARCHAR(20)
);

CREATE TABLE incidents (
    id SERIAL PRIMARY KEY,
    order_id VARCHAR(50),
    incident_type VARCHAR(50),
    severity VARCHAR(20),
    description TEXT
);