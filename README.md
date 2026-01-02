# devAi430 Data ETL Pipeline 🚀
[![Python](https://img.shields.io/badge/Python-3.9+-blue)]()
[![Airflow](https://img.shields.io/badge/Airflow-ETL-success)]()
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-Database-blue)]()
[![License](https://img.shields.io/badge/license-MIT-green.svg)]()

## 📘 Overview
The **devAi430 Data ETL Pipeline** demonstrates an end-to-end **Extract, Transform, Load (ETL)** workflow built using **Python** and **Apache Airflow**.  
It automates data ingestion, transformation, and loading into a **PostgreSQL** database, reflecting **devAi430’s data engineering expertise**.

---

## 🧱 Architecture Overview
```
Data Source → Extraction (Python) → Transformation (Cleaning/Formatting) → Load → PostgreSQL DB → Airflow DAG Scheduling
```

**Core Components:**
- `dags/` → Airflow DAG definitions
- `scripts/` → Python ETL scripts
- `data/` → Sample input data
- `config/` → Airflow environment setup

---

## ⚙️ Setup Instructions

### 1️⃣ Clone the repository
```bash
git clone https://github.com/devAi430/devAi430-data-etl-pipeline.git
cd devAi430-data-etl-pipeline
```

### 2️⃣ Create and activate a virtual environment
```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

### 3️⃣ Install dependencies
```bash
pip install -r requirements.txt
```

### 4️⃣ Configure PostgreSQL connection
Create a `.env` file in the project root with:
```bash
POSTGRES_USER=admin
POSTGRES_PASSWORD=password
POSTGRES_DB=etl_db
POSTGRES_HOST=localhost
POSTGRES_PORT=5432
```

### 5️⃣ Run Airflow locally
```bash
airflow db init
airflow webserver --port 8080
airflow scheduler
```
Access Airflow UI at [http://localhost:8080](http://localhost:8080)

---

## 🧠 Key Features
✅ Fully Python-based ETL pipeline  
✅ Orchestrated via Apache Airflow  
✅ PostgreSQL-ready setup  
✅ Modular, scalable, and easy to extend  
✅ Ready for cloud or Docker upgrade  

---

## 🤝 Credits
Originally adapted and enhanced under **devAi430** for internal and client-facing data engineering showcases.

---

## 📜 License
Distributed under the **MIT License**.  
© 2026 devAi430. All rights reserved.
