-- ============================================================
-- Topic: CREATE and DROP DATABASE
-- ============================================================

-- See what databases already exist on the server.
SHOW DATABASES;

-- Create a throwaway database just to demonstrate DROP.
CREATE DATABASE demo_scratch;
SHOW DATABASES;

-- DROP DATABASE permanently deletes the database and everything
-- inside it. Only do this if you no longer need the data!
DROP DATABASE demo_scratch;
SHOW DATABASES;

-- Now create the database we'll actually use for the next few
-- demo files (CREATE TABLE, INSERT, UPDATE, DELETE).
CREATE DATABASE seller;
USE seller;
