
import pandas as pd
import requests
from datetime import datetime
from airflow.models import Variable
from airflow.decorators import task
import sys
sys.path.insert(0, '/opt/airflow/plugins/scripts')
from plugins.scripts.town_mapping import town_mapping


@task
def fetch_meteo_data():
    """
    EXTRACT DATA FROM API OPENWEATHERMAP
    """
    API_KEY = Variable.get("API_KEY")
    records_data = []    #store data in a list
    for location_id, town in town_mapping.items():
        url = (
            "https://api.openweathermap.org/data/2.5/weather?"
            f"q={town}&units=metric&appid={API_KEY}"
        )

        data = requests.get(url, timeout=10).json()
        records_data.append({
            "location_id": location_id,
            "ville": data["name"],
            "temperature": data["main"]["temp"],
            "humidity": data["main"]["humidity"],
            "pression": data["main"]["pressure"],
            "weather": data["weather"][0]["main"],
            "temperature_max": data["main"]["temp_max"],
            "temperature_min": data["main"]["temp_min"],
            "temperature_feel": data["main"]["feels_like"],
            "wind_speed": data["wind"]["speed"],
            "rain_day": data.get("rain", {}).get("1h", 0),
            "cloud_rate": data["clouds"]["all"],
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        })

    """
    load data to CSV file and postgres
    """
    df = pd.DataFrame(records_data)
    current_date = datetime.now().strftime("%Y-%m-%d_%H:%M")
 
    "for docker"
    filename = f"/opt/airflow/airflow-export/weather_{current_date}.csv"
    df.to_csv(filename, index=False)
    return filename

    
