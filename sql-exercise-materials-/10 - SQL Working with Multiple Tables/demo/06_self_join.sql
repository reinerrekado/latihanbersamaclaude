-- ============================================================
-- Topic: SELF JOIN
-- A regular join where a table is joined with itself, using two
-- different aliases to tell the two "copies" apart.
--
-- SELECT column_name(s)
-- FROM table1 T1, table1 T2
-- WHERE condition;
-- ============================================================

USE sakila;

-- Find pairs of different films that share the exact same length.
-- T1 and T2 both point at "film" -- the alias is what lets us
-- treat them as two separate tables.
SELECT T1.title AS Film_A, T2.title AS Film_B, T1.length
FROM film T1, film T2
WHERE T1.film_id <> T2.film_id
  AND T1.length = T2.length
ORDER BY T1.length DESC
LIMIT 10;

-- Same query written with explicit JOIN syntax.
SELECT T1.title AS Film_A, T2.title AS Film_B, T1.length
FROM film T1
JOIN film T2
    ON T1.film_id <> T2.film_id
   AND T1.length = T2.length
ORDER BY T1.length DESC
LIMIT 10;

-- Self join on customer/address: find customers who live in the
-- same city as another customer.
SELECT C1.first_name AS Customer_A, C2.first_name AS Customer_B, A1.city_id
FROM customer C1
JOIN address A1 ON C1.address_id = A1.address_id
JOIN customer C2 ON C1.customer_id <> C2.customer_id
JOIN address A2 ON C2.address_id = A2.address_id
WHERE A1.city_id = A2.city_id
LIMIT 10;
