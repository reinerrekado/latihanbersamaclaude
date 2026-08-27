-- ============================================================
-- Topic: CREATE TABLE
-- ============================================================

USE seller;

-- Basic CREATE TABLE: column name + datatype for each column.
CREATE TABLE persons (
    PersonID  INT,
    LastName  VARCHAR(255),
    FirstName VARCHAR(255),
    Address   VARCHAR(255),
    City      VARCHAR(255)
);

DESCRIBE persons;

-- CREATE TABLE ... AS SELECT: copy a table (or a subset of columns/
-- rows) from an existing table, including its data.
-- We need world for this example, so this line uses the fully
-- qualified name world.city instead of switching databases.
CREATE TABLE seller.city_names AS
    SELECT Name, CountryCode
    FROM world.city
    WHERE CountryCode = 'IDN';

SELECT * FROM city_names LIMIT 5;
