import pandas as pd
from airflow.decorators import task
from datetime import datetime

@task
def load_historical_data() -> str:
    file_path = "/opt/raw/weather_historical.csv"
    df = pd.read_csv(file_path, encoding="utf-8", low_memory=False)

    # clear any unwanted characters in column names
    df.columns = [col.replace("Â", "°") for col in df.columns]

    df = df[df['time'] != 'time']

    df['location_id'] = pd.to_numeric(df['location_id'], errors='coerce').astype('Int64')
    df['time'] = pd.to_datetime(df['time'], errors='coerce')
    df = df.dropna(subset=['time'])

    column_mapping = {
        "temperature_2m (°C)": "temperature",
        "apparent_temperature (°C)": "apparent_temperature",
        "precipitation (mm)": "precipitation",
        "rain (mm)": "rain",
        "snowfall (cm)": "snowfall_cm",
        "weather_code (wmo code)": "weather_code",
        "wind_speed_10m (km/h)": "wind_speed",
        "wind_gusts_10m (km/h)": "wind_gusts",
        "cloud_cover (%)": "cloud_cover",
        "soil_temperature_0_to_7cm (°C)": "soil_temperature"
    }
    df = df.rename(columns=column_mapping)

    if 'snowfall_cm' in df.columns:
        df['snowfall_cm'] = pd.to_numeric(df['snowfall_cm'], errors='coerce').fillna(0)
        df['snow'] = df['snowfall_cm'] * 1.43
    else:
        df['snow'] = 0

    numeric_cols = [
        "temperature", "apparent_temperature", "precipitation", "rain",
        "wind_speed", "cloud_cover", "soil_temperature", "snow"
    ]
    for col in numeric_cols:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors="coerce")

    final_columns = [
        "location_id",
        "time",
        "temperature",
        "apparent_temperature",
        "precipitation",
        "rain",
        "snow",
        "weather_code",
        "wind_speed",
        "cloud_cover",
        "soil_temperature"
    ]

    df_historical = df[final_columns].copy()

    current_date = datetime.now().strftime("%Y-%m-%d_%H:%M")
    output_file = f"/home/tsioryr/HEI-Etudes/data-airflow/airflow/tmp/historical_weather_{current_date}.csv"

    df_historical.to_csv(output_file, index=False)
    return output_file