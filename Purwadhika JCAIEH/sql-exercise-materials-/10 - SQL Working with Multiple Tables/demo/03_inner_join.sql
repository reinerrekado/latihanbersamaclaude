-- ============================================================
-- Topic: (INNER) JOIN
-- Returns only the rows that have a matching value in both
-- tables. This is the JOIN type you reach for by default.
--
-- SELECT column_name(s)
-- FROM table1
-- INNER JOIN table2 ON table1.column_name = table2.column_name;
-- ============================================================

USE sakila;

-- Every customer paired with every payment they made.
-- A customer with zero payments simply won't appear.
SELECT customer.first_name, customer.last_name, payment.amount
FROM customer
INNER JOIN payment
    ON customer.customer_id = payment.customer_id;

-- "INNER" is optional -- plain JOIN means the same thing.
SELECT c.first_name, c.last_name, p.amount, p.payment_date
FROM customer c
JOIN payment p
    ON c.customer_id = p.customer_id
ORDER BY p.amount DESC
LIMIT 10;

-- Three-table inner join: film -> inventory -> rental tells us
-- which films have actually been rented out.
SELECT f.title, r.rental_date
FROM film f
JOIN inventory i ON f.film_id = i.film_id
JOIN rental r ON i.inventory_id = r.inventory_id
ORDER BY r.rental_date
LIMIT 10;
