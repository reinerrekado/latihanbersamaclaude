-- ============================================================
-- Topic: RIGHT (OUTER) JOIN
-- Returns every row from the right table, plus matching rows
-- from the left table. Where the left table has no match, its
-- columns come back NULL. In some databases this is written
-- RIGHT OUTER JOIN.
--
-- SELECT column_name(s)
-- FROM table1
-- RIGHT JOIN table2 ON table1.column_name = table2.column_name;
--
-- Note: a RIGHT JOIN is just a LEFT JOIN with the tables swapped
-- -- pick whichever reads more naturally for the question at hand.
-- ============================================================

USE sakila;

-- Same idea as the LEFT JOIN film/inventory demo, but written the
-- other way around: every inventory row, plus its film details.
-- (Every inventory row has a valid film_id, so nothing is NULL
-- here -- this direction has no "missing" side to show off.)
SELECT f.title, i.inventory_id, i.store_id
FROM inventory i
RIGHT JOIN film f
    ON i.film_id = f.film_id
ORDER BY f.title
LIMIT 10;

-- Same query, written as the equivalent LEFT JOIN -- compare the
-- two and notice the result is identical, only FROM/JOIN order
-- and keyword changed.
SELECT f.title, i.inventory_id, i.store_id
FROM film f
LEFT JOIN inventory i
    ON f.film_id = i.film_id
ORDER BY f.title
LIMIT 10;
