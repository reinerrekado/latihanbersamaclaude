-- ============================================================
-- Topic: Relational Model Constraints (Referencing, PK & FK)
-- A primary key (PK) uniquely identifies each row in its own
-- table and cannot be NULL. A foreign key (FK) is a column (or
-- set of columns) in one table that points at the PK of another
-- table -- that's how two tables "reference" each other.
--   Parent table    -> holds the PK being pointed at (e.g. city)
--   Dependent table -> holds the FK doing the pointing (e.g. address)
-- ============================================================

USE sakila;

SHOW TABLES;

-- DESCRIBE shows each column's key role:
--   PRI = primary key, MUL = part of a foreign key / non-unique index
DESCRIBE country;   -- country_id is PRI (parent table, no FKs of its own)
DESCRIBE city;      -- city_id is PRI, country_id is MUL (dependent on country)
DESCRIBE address;   -- address_id is PRI, city_id is MUL (dependent on city)
DESCRIBE customer;  -- customer_id is PRI, address_id is MUL (dependent on address)

-- SHOW CREATE TABLE prints the actual CONSTRAINT clauses MySQL
-- enforces -- this is where the FK -> PK relationship is spelled out.
SHOW CREATE TABLE address;

-- Referencing chain in Sakila:
--   country (parent) <- city (dependent of country, parent of address)
--        <- address (dependent of city, parent of customer)
--             <- customer (dependent of address)
-- Every FK column below must match a value that already exists
-- in the parent table's PK column -- that's the constraint at work.
SELECT country_id, country FROM country LIMIT 5;
SELECT city_id, city, country_id FROM city LIMIT 5;
SELECT address_id, address, city_id FROM address LIMIT 5;
SELECT customer_id, first_name, last_name, address_id FROM customer LIMIT 5;
