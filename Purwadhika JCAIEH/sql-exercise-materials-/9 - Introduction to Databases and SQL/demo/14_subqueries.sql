-- ============================================================
-- Topic: Sub-Queries and Nested SELECT
-- A sub-query is a SELECT nested inside another query — in the
-- WHERE clause, in the list of columns, or in the FROM clause.
-- ============================================================

USE world;

-- --- Sub-query in WHERE ---
-- You cannot write WHERE Population > AVG(Population) directly —
-- an aggregate function can't be evaluated row-by-row in WHERE.
-- Wrap it in a sub-query instead.
SELECT Name, Population
FROM country
WHERE Population > (SELECT AVG(Population) FROM country);

-- --- Sub-query in the column list (column expression) ---
-- Every row repeats the same sub-query result alongside its own data.
SELECT Name, LifeExpectancy,
       (SELECT MIN(LifeExpectancy) FROM country) AS Lowest_LifeExpectancy,
       (SELECT MAX(LifeExpectancy) FROM country) AS Highest_LifeExpectancy
FROM country
WHERE Region = 'Southeast Asia';

-- --- Sub-query in FROM (a "derived table") ---
-- Treat the result of a SELECT as if it were a table you can
-- query, filter, and alias.
SELECT *
FROM (
    SELECT Name, Continent, Population
    FROM country
    WHERE Continent = 'Asia'
) AS asia_countries
WHERE Population > 50000000;
