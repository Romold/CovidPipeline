# COVID-19 Data ETL Pipeline (Sri Lanka)

This project is a simple end-to-end ETL pipeline that fetches historical COVID-19 data for Sri Lanka, processes it into a structured format, and stores it for further analysis.

The pipeline is designed to be modular, readable, and easy to extend.

---


## Pipeline Overview

The pipeline follows a standard ETL workflow.

### Extract
- Fetches historical COVID-19 data for Sri Lanka from a public API
- Converts nested JSON timelines (cases, deaths, recovered) into tabular form
- Stores the raw dataset as a CSV file with a timestamped filename

### Transform
- Cleans and normalizes the extracted data
- Ensures consistent date formats and column naming
- Prepares the dataset for storage and analysis

### Load
- Loads the cleaned data into a SQLite database
- Persists the data for downstream querying or analytics use cases

---

## Data Source

- Public COVID-19 historical data API  
- Country scope: Sri Lanka  
- Granularity: Daily time series (cases, deaths, recoveries)


