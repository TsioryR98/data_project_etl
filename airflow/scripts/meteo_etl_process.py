import os
from fileinput import filename

import pandas as pd
import requests
from datetime import datetime

def fetch_meteo_data():
    """
    extract data from openweather for ETL
    """
    API_KEY = os.getenv("API_KEY")
    test_api_loc= "Paris"

    url= f"https://api.openweathermap.org/data/2.5/weather?q={test_api_loc}&units=metric&appid={API_KEY}"
    response = requests.get(url)
    data = response.json()

    """
    transform data from JSON
    """
    meteo = {
        "ville": data["name"],
        "temperature": data["main"]["temp"],
        "humidity": data["main"]["humidity"],
        "pression": data["main"]["pressure"],
        "weather": data["weather"][0]["main"],
        "description": data["weather"][0]["description"],
        "temperature_max": data["main"]["temp_max"],
        "temperature_min": data["main"]["temp_min"],
        "temperature_feel": data["main"]["feels_like"],
        "wind_speed": data["wind"]["speed"],
        "rain_day": data.get("rain", {}).get("1h", 0),
        "cloud_rate": data["clouds"]["all"],
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    df = pd.dataFrame([meteo])

    """
    load data to CSV file and postgres
    """
    current_date = datetime.now().strftime("%Y%m%d_%H%M")
    filename = f"/opt/airflow/airflow-export/weather_{current_date}.csv"

    df.to_csv(filename, index=False)

    
