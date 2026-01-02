from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import pandas as pd
import sqlite3
import numpy as np
import os


# Base directory 
BASE_DIR = "/home/joo/ETL_AIRFLOW_PROJECT"



# Extract
def extract_task():
    df = pd.read_csv(os.path.join(BASE_DIR, "data", "source.csv"))
    df.to_csv(os.path.join(BASE_DIR, "data", "extract.csv"), index=False)






def transform_task():
    df = pd.read_csv(os.path.join(BASE_DIR, "data", "extract.csv"))

    if "age" in df.columns:
        df["age"] = pd.to_numeric(df["age"], errors="coerce")
        df.loc[(df["age"] < 0) | (df["age"] > 120), "age"] = np.nan
        avg_age = df["age"].mean()
        df["age"] = df["age"].fillna(avg_age).astype("int64")

    if "salary" in df.columns:
        df["salary"] = pd.to_numeric(df["salary"], errors="coerce")
        median_salary = df["salary"].median()
        df.loc[(df["salary"] < 3000) | (df["salary"] > 50000), "salary"] = median_salary
        df["salary"] = df["salary"].fillna(median_salary)

    if "join_date" in df.columns:
        df["join_date"] = pd.to_datetime(df["join_date"], errors="coerce")
        df["join_date"] = df["join_date"].fillna(pd.to_datetime("2020-01-01"))

    if "city" in df.columns:
        df["city"] = df["city"].str.strip().str.title()
        df["city"] = df["city"].fillna("Unknown")



    if "id" in df.columns:
        df = df.sort_values(by="id")
    else:
        df.insert(0, "id", range(1, len(df) + 1))

    df.to_csv(os.path.join(BASE_DIR, "data", "transform.csv"), index=False)
    

    





# Load
def load_task():
    df = pd.read_csv(os.path.join(BASE_DIR, "data", "transform.csv"))
    conn = sqlite3.connect(os.path.join(BASE_DIR, "data", "db.sqlite"))
    df.to_sql("my_table", conn, if_exists="replace", index=False)
    conn.close()






# DAG Definition
with DAG(
    dag_id="ETL_Project",
    start_date=datetime(2025, 9, 8),
    schedule="@daily",
    catchup=False,
) as dag:


    t1 = PythonOperator(
        task_id="extract",
        python_callable=extract_task,
    )

    t2 = PythonOperator(
        task_id="transform",
        python_callable=transform_task,
    )

    t3 = PythonOperator(
        task_id="load",
        python_callable=load_task,
    )

    t1 >> t2 >> t3