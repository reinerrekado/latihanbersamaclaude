-- ============================================================
-- Topic: String Patterns with LIKE
-- % = zero, one, or many characters
-- _ = exactly one character
-- ============================================================

USE world;

-- Starts with 'Y'.
SELECT * FROM city WHERE District LIKE 'Y%';

-- Ends with 'x'.
SELECT * FROM city WHERE District LIKE '%x';

-- Starts with 'Y' AND ends with 'a'.
SELECT * FROM city WHERE Name LIKE 'Y%a';

-- Contains 'or' anywhere.
SELECT * FROM city WHERE Name LIKE '%or%';

-- Second character is 'r' (underscore = exactly one character).
SELECT * FROM city WHERE Name LIKE '_r%';
