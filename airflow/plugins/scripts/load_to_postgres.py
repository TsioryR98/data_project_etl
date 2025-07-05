import pandas as pd
from airflow.decorators import task
import os
from airflow.providers.postgres.hooks.postgres import PostgresHook


@task
def load_to_postgres(star_schema_dir: str, postgres_conn_id: str) -> None:
    """
    (dim_location, dim_time, fact_weather)
    for tables PostgreSQL .
    :param star_schema_dir
    :param pg_conn_string: c
    """
    hook = PostgresHook(postgres_conn_id=postgres_conn_id)
    conn = hook.get_conn()

    dim_location_path = os.path.join(star_schema_dir, "dim_location.csv")
    dim_time_path = os.path.join(star_schema_dir, "dim_time.csv")
    fact_weather_path = os.path.join(star_schema_dir, "fact_weather.csv")

    #  dim_location
    df_dim_location = pd.read_csv(dim_location_path)
    df_dim_location.to_sql("dim_location", engine, if_exists="replace", index=False)

    #  dim_time
    df_dim_time = pd.read_csv(dim_time_path)
    df_dim_time.to_sql("dim_time", engine, if_exists="replace", index=False)

    #  fact_weather
    df_fact_weather = pd.read_csv(fact_weather_path)
    df_fact_weather.to_sql("fact_weather", engine, if_exists="replace", index=False)
