CREATE TABLE IF NOT EXISTS orders (

    id SERIAL PRIMARY KEY,

    client_order_id VARCHAR(50),

    symbol VARCHAR(20),

    quantity INTEGER,

    price DECIMAL,

    status VARCHAR(20)

);


CREATE TABLE IF NOT EXISTS incidents (

    id SERIAL PRIMARY KEY,

    order_id VARCHAR(50),

    incident_type VARCHAR(50),

    severity VARCHAR(20),

    description TEXT

);


INSERT INTO orders
(client_order_id, symbol, quantity, price, status)
VALUES
('ORD001','AAPL',100,180.50,'FILLED'),
('ORD002','MSFT',50,320.20,'REJECTED'),
('ORD003','TSLA',20,250.00,'PENDING');


INSERT INTO incidents
(order_id, incident_type, severity, description)
VALUES
('ORD002',
'Order Rejection',
'MEDIUM',
'Exchange rejected order due to invalid symbol'),


('ORD003',
'Missing Execution',
'HIGH',
'No execution report received from exchange'),


('ORD004',
'Connectivity Issue',
'HIGH',
'Connection reset while sending order');