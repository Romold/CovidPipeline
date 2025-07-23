import requests
import pandas as pd
from datetime import datetime

def extract_data():
    url = 'https://disease.sh/v3/covid-19/historical/Sri%20Lanka?lastdays=all'
    response = requests.get(url)

    if response.status_code != 200:
        raise Exception(f"API request failed with status code {response.status_code}")

    data = response.json()
    country = data['country']
    timeline = data['timeline']

    # Convert nested data into DataFrames
    df_cases = pd.DataFrame(timeline['cases'].items(), columns=['Date', 'Cases'])
    df_deaths = pd.DataFrame(timeline['deaths'].items(), columns=['Date', 'Deaths'])
    df_recovered = pd.DataFrame(timeline['recovered'].items(), columns=['Date', 'Recovered'])

    # Merge the DataFrames
    df = df_cases.merge(df_deaths, on='Date').merge(df_recovered, on='Date')
    df['Country'] = country

    # Save raw file
    today = datetime.now().strftime("%Y-%m-%d")
    raw_path = f"data/raw_covid_{today}.csv"
    df.to_csv(raw_path, index=False)
    return raw_path
