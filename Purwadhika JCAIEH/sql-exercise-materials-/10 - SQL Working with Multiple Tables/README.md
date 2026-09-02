# 10 - SQL Working with Multiple Tables

Materials for the "SQL Working with Multiple Tables" session (Job Connector Program).
Source slides: `10 - SQL Working with Multiple Tables.pdf`.

## Folder structure

```
10 - SQL Working with Multiple Tables/
├── README.md                  <- you are here
├── demo/                      <- one file per slide topic, run in order during class
└── exercises/
    ├── exercises.sql          <- the 10 practice questions (unanswered) for students
    └── solutions.sql          <- answer key (instructor only)
```

## Setup

1. Install **MySQL Server** and **MySQL Workbench** (or use the `mysql` CLI client).
2. Import the **`sakila`** sample database, used throughout the demos and exercises. It's
   already included at `../data/sakila-db/` (`sakila-schema.sql` then `sakila-data.sql`)
   -- see the repo-root [README](../README.md#database-setup) for the install steps
   (connect with `mysql -u root -p`, then `SOURCE data/sakila-db/sakila-schema.sql;`
   followed by `SOURCE data/sakila-db/sakila-data.sql;`).
3. Confirm it loaded:
   ```sql
   SHOW DATABASES;
   USE sakila;
   SHOW TABLES;   -- actor, address, category, city, country, customer, film, ...
   ```
4. For the Python demo (`demo/07_python_mysql_connector.py`), also install the
   connector: `pip install mysql-connector-python pandas python-dotenv`.
5. Copy the repo-root `.env copy` file to `.env` (same folder) and fill in your
   real MySQL credentials — `.env` is git-ignored, `.env copy` is the tracked
   template. The demo script loads `DB_HOST`, `DB_USER`, `DB_PASSWORD`, and
   `DB_NAME` from it.

## Running the demo files

Open each file in `demo/` inside MySQL Workbench, in numbered order, and run it
statement by statement (highlight a statement, press `Cmd/Ctrl + Enter`) rather than
executing the whole file at once.

- `01` covers the relational model: primary keys, foreign keys, referencing, and the
  parent/dependent table terminology, inspected directly on Sakila's real tables and
  constraints (`DESCRIBE`, `SHOW CREATE TABLE`).
- `02` shows an implicit join (comma-separated `FROM` + `WHERE`) and why it becomes a
  Cartesian join without a matching condition.
- `03`–`06` cover explicit `JOIN` syntax: `INNER JOIN`, `LEFT JOIN`, `RIGHT JOIN`, and
  `SELF JOIN`, each demonstrated on Sakila tables (`film`, `inventory`, `customer`,
  `payment`, `address`).
- `07` is a Python script showing how to connect to `sakila` with
  `mysql-connector-python` and pull query results into a pandas DataFrame.

## Exercises

Students work through `exercises/exercises.sql` against the `sakila` database. Each
question is a comment above a blank spot for their query. Check answers against
`exercises/solutions.sql` -- note the solutions are *one* valid way to write each query,
not the only correct answer; equivalent queries that return the same result set are fine.
