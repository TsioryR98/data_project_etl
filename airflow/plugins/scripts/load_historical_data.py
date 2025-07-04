import pandas as pd
from datetime import datetime
from airflow.decorators import task


@task
def load_historical_data():
    """
    Load historical weather data from a CSV file.
    """
    file_path = "/home/tsioryr/HEI-Etudes/data-airflow/raw/weather_historical.csv"

    df = pd.read_csv(file_path)

    df['timeS'] = pd.to_datetime(df['timeS'])

    df = df.rename(
        columns={
            "temperature_2m (Â°C)": "temperature",
            "apparent_temperature (Â°C)": "apparent_temperature",
            "precipitation (mm)": "precipitation",
            "rain (mm)": "rain",
            "snowfall (cm)": "snowfall",
            "weather_code (wmo code)": "weather_code",
            "wind_speed_10m (km/h)": "wind_speed",
            #"wind_gusts_10m (km/h)": "wind_gusts", #to delete
            "cloud_cover (%)": "cloud_cover",
            "soil_temperature_0_to_7cm (Â°C)": "soil_temperature"
        },
        inplace=True)
    return df
