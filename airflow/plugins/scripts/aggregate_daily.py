import pandas as pd
from airflow.decorators import task
from datetime import datetime

@task
def aggregate_daily(combined_csv: str) -> str:
    """
    DAILY AGGREGATION OF METEOROLOGICAL DATA from a combined CSV file.
    """
    df = pd.read_csv(combined_csv)

    df["time"] = pd.to_datetime(df["time"], errors="coerce")

    df["date"] = df["time"].dt.date

    agg_columns = [
        "apparent_temperature", "cloud_cover", "precipitation",
        "rain", "snow", "soil_temperature", "temperature", "wind_speed"
    ]

    df_daily = df.groupby(["location_id", "city", "date"])[agg_columns].mean().reset_index()

    df_daily[agg_columns] = df_daily[agg_columns].round(3)     # 3 decimal places

    #ordered columns
    ordered_cols = [
        "location_id", "city", "apparent_temperature", "cloud_cover", "precipitation",
        "rain", "snow", "soil_temperature", "temperature", "wind_speed", "date"
    ]
    ordered_cols = [col for col in ordered_cols if col in df_daily.columns]
    df_daily = df_daily[ordered_cols]

    current_date = datetime.now().strftime("%Y-%m-%d_%H:%M")
    output_file = f"/home/tsioryr/HEI-Etudes/data-airflow/airflow/data/aggregated_daily_{current_date}.csv"
    df_daily.to_csv(output_file, index=False)

    return output_file
