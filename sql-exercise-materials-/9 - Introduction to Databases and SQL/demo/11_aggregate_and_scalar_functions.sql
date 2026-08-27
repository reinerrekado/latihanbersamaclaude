-- ============================================================
-- Topic: Built-in Functions
-- Aggregate functions (SUM, COUNT, AVG, MIN, MAX) collapse many
-- rows into one value. Scalar functions (ROUND, LENGTH, UCASE,
-- LCASE) transform each row's value individually.
-- ============================================================

USE world;

-- --- Aggregate functions ---

SELECT SUM(Population) AS Total_Population
FROM city
WHERE CountryCode = 'IDN';

SELECT COUNT(Name) AS Total_City
FROM city
WHERE CountryCode = 'IDN';

SELECT AVG(Population) AS Avg_Population
FROM city
WHERE CountryCode = 'IDN';

SELECT MIN(Population) AS Min_Population, MAX(Population) AS Max_Population
FROM city
WHERE CountryCode = 'IDN';

-- --- Scalar functions ---

-- ROUND(number, decimals) — decimals is optional, defaults to 0.
SELECT Name, ROUND(LifeExpectancy) FROM country;

SELECT Name, Region,
       ROUND(Population / SurfaceArea, 2) AS Population_Density
FROM country
WHERE Region = 'Southeast Asia';

-- LENGTH() — string length in bytes.
SELECT Name, LENGTH(Name) AS Length_Name
FROM country
WHERE Region = 'Southeast Asia'
ORDER BY Length_Name DESC;

-- UCASE()/UPPER() and LCASE()/LOWER().
SELECT UCASE(Name), Population
FROM country
WHERE Region = 'Southeast Asia'
ORDER BY Population DESC;

SELECT LCASE(Name), Population
FROM country
WHERE Region = 'Southeast Asia'
ORDER BY Population DESC;
