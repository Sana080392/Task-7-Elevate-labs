CREATE DATABASE IF NOT EXISTS sales_demo;
USE sales_demo;

CREATE TABLE IF NOT EXISTS sales (
    id INT AUTO_INCREMENT PRIMARY KEY,
    product VARCHAR(50),
    quantity INT,
    price DECIMAL(10,2)
);

INSERT INTO sales (product, quantity, price) VALUES
('Apples', 10, 1.50),
('Bananas', 20, 1.00),
('Oranges', 15, 2.00),
('Grapes', 5, 3.00);
