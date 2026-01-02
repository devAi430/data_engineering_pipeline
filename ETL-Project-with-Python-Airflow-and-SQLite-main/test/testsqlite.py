import sqlite3
import pandas as pd


conn = sqlite3.connect("/home/joo/ETL_AIRFLOW_PROJECT/data/db.sqlite")


df = pd.read_sql("SELECT * FROM my_table LIMIT 10;", conn)

print(df)

conn.close()
