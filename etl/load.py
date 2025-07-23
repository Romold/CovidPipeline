import pandas as pd
import sqlite3

def load_data(clean_file_path):
    df = pd.read_csv(clean_file_path)

    conn = sqlite3.connect("db/covid_data.db")
    df.to_sql("covid_data", conn, if_exists="append", index=False)
    conn.commit()
    conn.close()
