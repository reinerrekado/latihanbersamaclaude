-- ============================================================
-- Topic: LEFT (OUTER) JOIN
-- Returns every row from the left table, plus matching rows
-- from the right table. Where the right table has no match,
-- its columns come back NULL. In some databases this is written
-- LEFT OUTER JOIN.
--
-- SELECT column_name(s)
-- FROM table1
-- LEFT JOIN table2 ON table1.column_name = table2.column_name;
-- ============================================================

USE sakila;

-- Every film, plus its inventory row if it has one.
-- Films that were never stocked show a NULL inventory_id.
SELECT f.title, i.inventory_id, i.store_id
FROM film f
LEFT JOIN inventory i
    ON f.film_id = i.film_id
ORDER BY f.title
LIMIT 10;

-- Isolate exactly those "never stocked" films with a WHERE
-- clause filtering on the NULL that only LEFT JOIN can produce.
SELECT f.title
FROM film f
LEFT JOIN inventory i
    ON f.film_id = i.film_id
WHERE i.inventory_id IS NULL
ORDER BY f.title;

-- Every customer, plus their payments if any exist -- useful for
-- spotting customers who have never paid for anything.
SELECT c.first_name, c.last_name, p.amount
FROM customer c
LEFT JOIN payment p
    ON c.customer_id = p.customer_id
WHERE p.payment_id IS NULL;
