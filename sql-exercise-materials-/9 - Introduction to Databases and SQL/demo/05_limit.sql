-- ============================================================
-- Topic: LIMIT
-- ============================================================

USE world;

-- First 3 rows, in whatever order the table happens to store them.
SELECT * FROM city LIMIT 3;

SELECT * FROM city LIMIT 5;

-- LIMIT is most useful (and predictable) combined with ORDER BY —
-- we'll revisit this once ORDER BY is covered.
SELECT Name, Population FROM city ORDER BY Population DESC LIMIT 5;
