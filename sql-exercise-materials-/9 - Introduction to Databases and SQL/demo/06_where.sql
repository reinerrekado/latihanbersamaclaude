-- ============================================================
-- Topic: WHERE
-- ============================================================

USE world;

-- Numeric comparison.
SELECT * FROM city WHERE Population > 1000000;

-- Text match (exact).
SELECT * FROM city WHERE CountryCode = 'IDN';

-- Text pattern match with a wildcard (LIKE is covered in depth
-- in 08_like_string_patterns.sql — this is just a preview).
SELECT * FROM city WHERE Name LIKE 'X%';

-- Combining conditions with AND / OR.
SELECT * FROM city WHERE CountryCode = 'IDN' AND Population > 500000;
SELECT * FROM city WHERE CountryCode = 'IDN' OR CountryCode = 'MYS';
