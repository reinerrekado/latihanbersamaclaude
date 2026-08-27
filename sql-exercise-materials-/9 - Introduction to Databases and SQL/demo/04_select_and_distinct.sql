-- ============================================================
-- Topic: SELECT and SELECT DISTINCT
-- From here on we switch to the "world" sample database, which
-- has enough rows to make these demos meaningful.
-- ============================================================

USE world;

SHOW TABLES;

-- All columns, all rows.
SELECT * FROM city;

-- Only the columns you need.
SELECT Name, District, Population FROM city;

-- SELECT DISTINCT: unique values only. Compare the row counts.
SELECT District FROM city WHERE CountryCode = 'IDN';          -- has duplicates
SELECT DISTINCT District FROM city WHERE CountryCode = 'IDN'; -- duplicates removed
