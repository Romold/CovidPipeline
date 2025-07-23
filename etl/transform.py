import pandas as pd

def transform_data(raw_file_path):
    df = pd.read_csv(raw_file_path)

    # Convert string date like '1/22/20' to ISO format
    df['Date'] = pd.to_datetime(df['Date'], format='%m/%d/%y')

    # Optional: sort by date
    df = df.sort_values('Date')

    # Drop missing values if any
    df = df.dropna()

    # Save clean file
    clean_path = raw_file_path.replace("raw_", "clean_")
    df.to_csv(clean_path, index=False)
    return clean_path
