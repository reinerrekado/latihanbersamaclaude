-- ============================================================
-- Topic: UPDATE and DELETE
-- Uses the seller.persons table created in 02/03. Run those
-- first if this is a fresh session.
-- ============================================================

USE seller;

SELECT * FROM persons;

-- UPDATE: always pair with WHERE, or you'll update every row!
UPDATE persons
SET Address = 'Jln. Melati', City = 'DKI'
WHERE PersonID = 1;

SELECT * FROM persons WHERE PersonID = 1;

UPDATE persons
SET LastName = 'Andrea', FirstName = 'Robert'
WHERE PersonID = 2;

SELECT * FROM persons;

-- DELETE: same rule — always pair with WHERE, or the table is
-- emptied entirely.
DELETE FROM persons WHERE PersonID = 4;

SELECT * FROM persons;

-- What NOT to do (commented out on purpose): this deletes every
-- row in the table because there's no WHERE clause.
-- DELETE FROM persons;
