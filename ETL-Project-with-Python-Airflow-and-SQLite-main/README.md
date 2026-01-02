
📌 devAi430 Data ETL Pipeline with Airflow, Python, and PostgreSQL

🔹 Overview

This project demonstrates a complete ETL (Extract, Transform, Load) pipeline using Apache Airflow and Python.
The pipeline extracts data from CSV files, applies transformations, and loads the processed data into a PostgreSQL database.

It is designed to showcase fundamental data engineering skills, including data pipelines, orchestration, and testing.


---

📂 Project Structure

ETL_AIRFLOW_PROJECT/
 ├── dags/
 │   ├── etl_pipeline.py       # Main Airflow DAG for ETL
 │   └── testdag.py            # Sample/Test DAG
 ├── data/
 │   ├── db.sqlite             # PostgreSQL database
 │   ├── extract.csv           # Extracted raw data
 │   ├── source.csv            # Source data file
 │   └── transform.csv         # Transformed data
 ├── test/
 │   ├── employees_clean.csv   # Cleaned employee dataset (for testing)
 │   ├── test_etl.py           # Unit tests for ETL pipeline
 │   └── testsqlite.py         # Database connection tests
 └── README.md                 # Project documentation


---

🚀 Features

Extract data from CSV files

Transform data (cleaning & formatting)

Load data into PostgreSQL database

Airflow DAGs to orchestrate the pipeline

Unit tests for pipeline and database validation



---

⚙ Technologies Used

Python 3

Apache Airflow

PostgreSQL

CSV (pandas for handling data)


