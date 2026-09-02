-- ============================================================
-- Topic: GROUP BY and HAVING
-- GROUP BY collapses rows that share a value into one summary
-- row per group, usually alongside an aggregate function.
-- HAVING filters groups AFTER grouping (WHERE filters rows
-- BEFORE grouping — WHERE can't reference an aggregate).
-- ============================================================

USE world;

-- How many cities per country?
SELECT COUNT(ID) AS City_Count, CountryCode
FROM city
GROUP BY CountryCode;

-- WHERE + GROUP BY: filter rows first, then group what's left.
SELECT AVG(Population) AS Rata_rata, District AS Provinsi
FROM city
WHERE CountryCode = 'IDN'
GROUP BY District;

-- GROUP BY + HAVING: filter the *groups* using the aggregate result.
SELECT AVG(Population) AS Rata_rata, District AS Provinsi
FROM city
WHERE CountryCode = 'IDN'
GROUP BY District
HAVING Rata_rata > 500000;

-- HAVING can also filter on the grouped column itself.
SELECT AVG(Population) AS Rata_rata, District AS Provinsi
FROM city
WHERE CountryCode = 'IDN'
GROUP BY District
HAVING Provinsi LIKE 'K%';
