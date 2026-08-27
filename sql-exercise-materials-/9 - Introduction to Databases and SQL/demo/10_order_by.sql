-- ============================================================
-- Topic: ORDER BY
-- Default is ascending (ASC); use DESC for descending.
-- ============================================================

USE world;

SELECT * FROM city ORDER BY Name;

SELECT * FROM city ORDER BY Name DESC;

-- Sort by multiple columns: first by CountryCode, then by
-- Population (descending) within each country.
SELECT Name, CountryCode, Population
FROM city
ORDER BY CountryCode ASC, Population DESC;

-- ORDER BY + LIMIT together: "top N" queries.
SELECT Name, Population FROM city ORDER BY Population DESC LIMIT 5;
