COVID-19 Data ETL Pipeline (Sri Lanka)

This project is a simple end-to-end ETL pipeline that fetches historical COVID-19 data for Sri Lanka, processes it into a structured format, and stores it for further analysis.

The pipeline is designed to be modular, readable, and easy to extend.

Project Structure
.
├── data/
│   ├── raw_covid_YYYY-MM-DD.csv
│   └── clean_covid_YYYY-MM-DD.csv
├── db/
│   └── covid_data.db
├── etl/
│   ├── extract.py
│   ├── transform.py
│   ├── load.py
│   └── __init__.py
├── logs/
├── run_pipeline.py
├── requirements.txt
└── README.md

Pipeline Overview

The pipeline follows a standard ETL workflow:

1. Extract

Fetches historical COVID-19 data for Sri Lanka from a public API.

Converts nested JSON timelines (cases, deaths, recovered) into tabular form.

Stores the raw dataset as a CSV file with a timestamped filename.

2. Transform

Cleans and normalizes the extracted data.

Ensures consistent date formats and column naming.

Prepares the dataset for storage and analysis.

3. Load

Loads the cleaned data into a SQLite database.

Persists the data for downstream querying or analytics use cases.

Data Source

Public COVID-19 historical data API

Country scope: Sri Lanka

Granularity: Daily time series (cases, deaths, recoveries)

How to Run

Create and activate a virtual environment

python -m venv venv
source venv/bin/activate  # Linux / macOS
venv\Scripts\activate     # Windows


Install dependencies

pip install -r requirements.txt


Run the pipeline

python run_pipeline.py


This will:

Fetch the latest available historical data

Save raw and cleaned CSV files

Update the SQLite database

Output

Raw data: data/raw_covid_YYYY-MM-DD.csv

Cleaned data: data/clean_covid_YYYY-MM-DD.csv

Database: db/covid_data.db

Design Notes

Clear separation of extract, transform, and load stages

File-based outputs for transparency and debugging

SQLite used for simplicity and portability

Easily extendable to support additional countries or data sources

Possible Extensions

Add incremental loading logic

Introduce basic data validation checks

Schedule the pipeline using cron or a workflow orchestrator

Add analytical queries or dashboards on top of the database
