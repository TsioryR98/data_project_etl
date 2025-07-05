import pandas as pd
from airflow.decorators import task
from datetime import datetime
import sys

sys.path.insert(0, '/home/tsioryr/HEI-Etudes/data-airflow/airflow/plugins')
from scripts.town_mapping import town_mapping

@task
def clean_and_merged_data(historical_csv: str, openweather_csv: str) -> str:
    df_historical = pd.read_csv(historical_csv)
    df_recent = pd.read_csv(openweather_csv)

    #force to convert columns to numeric and datetime
    df_historical["time"] = pd.to_datetime(df_historical["time"], errors="coerce")
    df_recent["time"] = pd.to_datetime(df_recent["time"], errors="coerce")

    all_cols = sorted(set(df_historical.columns) | set(df_recent.columns))
    for col in all_cols:
        if col not in df_historical.columns:
            df_historical[col] = pd.NA
        if col not in df_recent.columns:
            df_recent[col] = pd.NA

    df_concat = pd.concat([df_historical[all_cols], df_recent[all_cols]], ignore_index=True)

    column_to_add = ["humidity", "pressure", "city", "weather"]
    df_with_new_column = df_recent[["location_id", "time"] + column_to_add].drop_duplicates()

    df_combined_data = df_concat.merge(
        df_with_new_column,
        on=["location_id", "time"],
        how="left",
        suffixes=("", "_src")
    )

    for col in column_to_add:
        df_combined_data[col] = df_combined_data[col].combine_first(df_combined_data[f"{col}_src"])
        df_combined_data.drop(columns=f"{col}_src", inplace=True)

    df_combined_data["city"] = df_combined_data["location_id"].map(town_mapping)

    df_combined_data.sort_values(["location_id", "time"], inplace=True)
    df_combined_data.drop_duplicates(subset=["location_id", "time"], keep="last", inplace=True)

    # drop  columns
    cols_to_drop = ["humidity", "pressure", "temperature_max", "temperature_min", "weather","weather_code",]
    df_combined_data = df_combined_data.drop(columns=[col for col in cols_to_drop if col in df_combined_data.columns])

    ordered_cols = [
        "location_id", "city","apparent_temperature", "cloud_cover", "precipitation",
        "rain", "snow", "soil_temperature", "temperature", "wind_speed", "time"
    ]

    ordered_cols = [col for col in ordered_cols if col in df_combined_data.columns]
    df_combined_data = df_combined_data[ordered_cols]

    current_date = datetime.now().strftime("%Y-%m-%d_%H:%M")
    file_output = f"/home/tsioryr/HEI-Etudes/data-airflow/airflow/data/combined_weather_{current_date}.csv"

    df_combined_data.to_csv(file_output, index=False)
    return file_output