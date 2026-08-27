-- ============================================================
-- Topic: INSERT INTO
-- ============================================================

USE seller;

-- Method 1: specify column names explicitly (safest — order and
-- completeness of columns doesn't matter as much).
INSERT INTO persons (PersonID, LastName, FirstName, Address, City)
VALUES (1, 'Andrew', 'Michael', 'Jln. Mawar', 'BSD');

-- Method 2: omit column names — values must be given for every
-- column, in the exact order the table was created.
INSERT INTO persons
VALUES (2, 'Zidane', 'Zinedine', 'Jln. Anggrek', 'DKI');

-- A couple more rows so UPDATE/DELETE demos have something to work with.
INSERT INTO persons (PersonID, LastName, FirstName, Address, City)
VALUES
    (3, 'Silva', 'David', 'Jln. Kenanga', 'Bandung'),
    (4, 'Aguero', 'Sergio', 'Jln. Melati', 'Surabaya');

SELECT * FROM persons;
