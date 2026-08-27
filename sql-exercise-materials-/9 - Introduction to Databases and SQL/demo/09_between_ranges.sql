-- ============================================================
-- Topic: BETWEEN (inclusive ranges)
-- ============================================================

USE world;

-- Numeric range, both endpoints included.
SELECT Name, Population
FROM city
WHERE Population BETWEEN 1000000 AND 2000000;

SELECT Name, Region, LifeExpectancy
FROM country
WHERE LifeExpectancy BETWEEN 80 AND 90;

-- NOT BETWEEN: everything outside the range.
SELECT Name, Region, LifeExpectancy
FROM country
WHERE LifeExpectancy NOT BETWEEN 45 AND 90;
