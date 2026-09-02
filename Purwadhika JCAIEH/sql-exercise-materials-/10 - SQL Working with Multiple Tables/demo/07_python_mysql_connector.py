# ============================================================
# Topic: Accessing a Database from Python with mysql-connector-python
# Install once:  pip install mysql-connector-python pandas python-dotenv
# Docs: https://dev.mysql.com/doc/connector-python/en/connector-python-introduction.html
#
# Credentials are read from a ".env" file at the repo root (see
# ".env copy" for the template) instead of being hardcoded here.
# ============================================================

import os

import mysql.connector
import pandas as pd
from dotenv import load_dotenv

load_dotenv()

# --- Create Connection -----------------------------------------
mydb = mysql.connector.connect(
    host=os.getenv("DB_HOST"),
    user=os.getenv("DB_USER"),
    passwd=os.getenv("DB_PASSWORD"),
    database='sakila',
)

# --- Method 1: run one query by hand -----------------------------
mycursor = mydb.cursor()

query = "SELECT * FROM film LIMIT 5"

mycursor.execute(query)
result = mycursor.fetchall()

df = pd.DataFrame(result, columns=mycursor.column_names)
print(df.head())

# --- Method 2: wrap it in a reusable function --------------------
# Write any query as a string, pass it in, get a DataFrame back.
def sql_df(your_query):
    mycursor.execute(your_query)
    myresult = mycursor.fetchall()
    df = pd.DataFrame(myresult, columns=mycursor.column_names)
    return df


# Try it against the exercises in this module, e.g.:
sql_df(
    """
    SELECT customer_id, rental_id, amount, payment_date
    FROM payment
    LIMIT 10
    """
)
