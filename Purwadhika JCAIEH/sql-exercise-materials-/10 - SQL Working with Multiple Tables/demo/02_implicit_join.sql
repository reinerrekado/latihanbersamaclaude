-- ============================================================
-- Topic: Implicit JOIN
-- Listing two tables in FROM, separated by a comma, joins them.
-- With no filter this is a full/Cartesian join: every row in
-- table1 is paired with every row in table2.
-- ============================================================

USE sakila;

-- Cartesian join: 599 customers x thousands of payments = a huge,
-- mostly meaningless result set. Run this once just to see the
-- row count explode, then move on.
SELECT COUNT(*) AS cartesian_row_count
FROM customer, payment;

-- Add a WHERE condition to keep only the rows where the two
-- tables actually relate to each other (customer_id matches).
SELECT *
FROM customer, payment
WHERE customer.customer_id = payment.customer_id;

-- Shorter aliases make this easier to read.
SELECT *
FROM customer C, payment P
WHERE C.customer_id = P.customer_id;

-- Prefix select-list columns with the alias once you have one --
-- especially important when both tables share a column name
-- (both customer and payment have customer_id).
SELECT C.first_name, C.last_name, P.amount, P.payment_date
FROM customer C, payment P
WHERE C.customer_id = P.customer_id
ORDER BY P.payment_date
LIMIT 10;
