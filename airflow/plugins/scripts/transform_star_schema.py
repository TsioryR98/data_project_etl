import pandas as pd
import os
from datetime import datetime
from airflow.decorators import task

@task
def transform_star_schema(combined_csv: str) -> str:
    """
    TRANSFORM DATA INTO STAR SCHEMA FORMAT
    Fact Table: `fact_weather_daily`
    Dimension Tables: `dim_location`, `dim_time` `dim_weather` if possible,
    """

    folder_date = datetime.now().strftime("%Y-%m-%d")       # snapshot label
    base_dir= "/home/tsioryr/HEI-Etudes/data-airflow/airflow/data/star-schema"
    output_dir= f"{base_dir}/{folder_date}"
    os.makedirs(output_dir, exist_ok=True)      # if not exist, create the directory

    df_transform = pd.read_csv(combined_csv)
    df_transform["date"] = pd.to_datetime(df_transform["date"], errors="coerce")

    #dim_location
    dim_location = (
        df_transform[["location_id", "city"]]
        .drop_duplicates()
        .sort_values("location_id")
        .reset_index(drop=True)
    )
    dim_location.to_csv(f"{output_dir}/dim_location.csv", index=False)

    #dim_time
    unique_dates = pd.DataFrame(df_transform["date"].unique(), columns=["date"])
    unique_dates["date"] = pd.to_datetime(unique_dates["date"])
    unique_dates["date_id"] = unique_dates["date"].dt.strftime("%Y%m%d").astype(int)
    unique_dates["year"] = unique_dates["date"].dt.year
    unique_dates["month"] = unique_dates["date"].dt.month
    unique_dates["day"] = unique_dates["date"].dt.day
    unique_dates["day_of_week"] = unique_dates["date"].dt.dayofweek
    unique_dates["quarter"] = unique_dates["date"].dt.quarter
    dim_time = unique_dates.sort_values("date").reset_index(drop=True)
    dim_time.to_csv(f"{output_dir}/dim_time.csv", index=False)


    measure_cols = [
        "apparent_temperature", "cloud_cover", "precipitation",
        "rain", "snow", "soil_temperature", "temperature", "wind_speed"
    ]
    df_transform = df_transform.merge(dim_time[["date", "date_id"]], on="date", how="left")
    #weather fact
    fact_weather = (
        df_transform[["location_id", "date_id"] + measure_cols]
        .copy() # new df
    )
    fact_weather.to_csv(f"{output_dir}/fact_weather.csv", index=False)

    return output_dir