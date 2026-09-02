-- ============================================================
-- Topic: Date and Time Functions
-- The "world" database doesn't have a proper DATE column, so we
-- build a small scratch table with sample payment dates — same
-- idea as the PAYMENT table in the slides, no extra sample DB
-- download required.
-- ============================================================

USE seller;

CREATE TABLE IF NOT EXISTS demo_payment (
    customer_id  INT,
    staff_id     INT,
    amount       DECIMAL(5,2),
    payment_date DATE
);

INSERT INTO demo_payment (customer_id, staff_id, amount, payment_date) VALUES
    (13,  1, 12.99, '2005-05-29'),
    (116, 1, 15.50, '2005-06-21'),
    (195, 2,  9.99, '2005-07-23'),
    (196, 1, 20.00, '2005-08-25'),
    (204, 2, 11.99, '2005-08-22'),
    (237, 1,  4.99, '2006-02-02'),
    (305, 1, 11.99, '2005-05-17'),
    (362, 1, 11.99, '2005-06-21'),
    (591, 2,  7.99, '2005-07-07'),
    (592, 2,  6.99, '2005-08-06');

SELECT * FROM demo_payment;

-- DAY(), MONTH(), YEAR() pull a single component out of a date.
SELECT customer_id, DAY(payment_date)
FROM demo_payment
WHERE amount > 11;

SELECT SUM(amount) AS Total_Amount_August
FROM demo_payment
WHERE MONTH(payment_date) = 8;

SELECT YEAR(payment_date) AS Year_Sales,
       AVG(amount) AS Average_Amount_Yearly
FROM demo_payment
GROUP BY Year_Sales;

-- DAYNAME()/MONTHNAME() return the name instead of the number.
SELECT AVG(amount) AS Average_Amount, DAYNAME(payment_date) AS Day_Name
FROM demo_payment
GROUP BY Day_Name
ORDER BY Average_Amount;

SELECT AVG(amount) AS Average_Amount, MONTHNAME(payment_date) AS Month_Name
FROM demo_payment
GROUP BY Month_Name
ORDER BY Average_Amount;

-- Date arithmetic: DATE(x) + N adds N days.
SELECT customer_id, amount,
       DAYNAME(DATE(payment_date) + 1) AS One_Day_After_Payment
FROM demo_payment
WHERE staff_id = 1 AND amount > 11;
