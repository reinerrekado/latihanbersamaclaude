# SQL Exercise Materials

Slides, demo scripts, and exercises for the SQL sessions of the Purwadhika Job
Connector Program.

## Folder structure

```
SQL Exercise Materials/
├── README.md                                <- you are here
├── .env copy                                 <- template MySQL credentials (copy to .env)
├── data/                                     <- sample databases used by the modules below
│   ├── sakila-db/
│   │   ├── sakila-schema.sql
│   │   └── sakila-data.sql
│   └── world-db/
│       └── world.sql
├── 9 - Introduction to Databases and SQL/    <- uses the "world" database
└── 10 - SQL Working with Multiple Tables/    <- uses the "sakila" database
```

## Database setup

Both sample databases needed for these modules are already included under `data/`,
so there's no need to download anything separately. Install them with the official
`mysql` command-line client:

1. Open a terminal in this repo's root folder (`SQL Exercise Materials/`).
2. Connect to the MySQL server using the `mysql` command-line client:
   ```
   $> mysql -u root -p
   ```
   Enter your password when prompted. A non-`root` account can be used, provided
   that the account has privileges to create new databases.
3. Load whichever database(s) you need for the module you're working through:

   **`world`** (used by `9 - Introduction to Databases and SQL/`):
   ```sql
   mysql> SOURCE data/world-db/world.sql;
   ```

   **`sakila`** (used by `10 - SQL Working with Multiple Tables/`) — execute the
   schema script first to create the database structure, then the data script to
   populate it:
   ```sql
   mysql> SOURCE data/sakila-db/sakila-schema.sql;
   mysql> SOURCE data/sakila-db/sakila-data.sql;
   ```

   Each script creates its own database (`DROP`/`CREATE DATABASE` is built into the
   scripts), so there's no separate `CREATE DATABASE` step. If `mysql` was started
   from a different working directory, replace the relative paths above with the
   actual paths to the files on your system.
4. Confirm a database loaded correctly:
   ```sql
   SHOW DATABASES;
   USE world;    -- or: USE sakila;
   SHOW TABLES;
   ```

## Credentials for the Python demos

Some demo scripts (e.g. `10 - SQL Working with Multiple Tables/demo/07_python_mysql_connector.py`)
connect via `mysql-connector-python` using credentials from a `.env` file:

1. Copy `.env copy` to `.env` (same folder, repo root).
2. Fill in your real MySQL host/user/password in `.env`.

`.env` is git-ignored; `.env copy` is the tracked template.

## Modules

Each numbered module folder has its own `README.md` with setup notes specific to
that session, a `demo/` folder (one file per slide topic, meant to be run in order
during class), and an `exercises/` folder (`exercises.sql` for students,
`solutions.sql` as the instructor-only answer key).
