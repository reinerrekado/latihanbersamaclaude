# 9 - Introduction to Databases and SQL

Materials for the "Introduction to Databases and SQL" session (Job Connector Program).
Source slides: `9 - Introduction to _Databases and SQL.pdf`.

## Folder structure

```
9 - Introduction to Databases and SQL/
├── README.md                  <- you are here
├── demo/                      <- one .sql file per slide topic, run in order during class
└── exercises/
    ├── exercises.sql          <- the 9 practice questions (unanswered) for students
    └── solutions.sql          <- answer key (instructor only)
```

## Setup

1. Install **MySQL Server** and **MySQL Workbench** (or use the `mysql` CLI client shown in
   the slides — Windows Start menu → "MySQL 8.0 Command Line Client").
2. Import the **`world`** sample database, used throughout the demos and exercises. It's
   already included at `../data/world-db/world.sql` — see the repo-root
   [README](../README.md#database-setup) for the install steps (connect with
   `mysql -u root -p`, then `SOURCE data/world-db/world.sql;`). In Workbench you can
   instead use `Server > Data Import`, or open the file as a script
   (`File > Open SQL Script`, then the lightning-bolt "Execute" button).
3. Confirm it loaded:
   ```sql
   SHOW DATABASES;
   USE world;
   SHOW TABLES;   -- city, country, countrylanguage
   ```

## Running the demo files

Open each file in `demo/` inside MySQL Workbench, in numbered order, and run it
statement by statement (highlight a statement, press `Cmd/Ctrl + Enter`) rather than
executing the whole file at once — the point is to show the result grid change after
each query and narrate what happened.

- `01`–`02` create a scratch `seller` database and a `persons` table (mirrors the
  slides) to demonstrate `CREATE`/`DROP DATABASE`, `CREATE TABLE`, `INSERT`, `UPDATE`,
  `DELETE` without touching the `world` sample data.
- `03` onward switch to `USE world;` and query the real `city` / `country` /
  `countrylanguage` tables for `SELECT`, filtering, sorting, functions, grouping, and
  subqueries.

## Exercises

Students work through `exercises/exercises.sql` against the `world` database. Each
question is a comment above a blank spot for their query. Check answers against
`exercises/solutions.sql` — note the solutions are *one* valid way to write each query,
not the only correct answer; equivalent queries that return the same result set are fine.
