from airflow import DAG
from datetime import datetime, timedelta
import sys

sys.path.insert(0, '/home/tsioryr/HEI-Etudes/data-airflow/airflow/plugins')
from scripts.fetch_meteo_data import fetch_meteo_data
from scripts.load_historical_data import load_historical_data
from scripts.clean_and_merged_data import clean_and_merged_data
from scripts.aggregate_daily import aggregate_daily
from scripts.transform_star_schema import transform_star_schema
from scripts.load_to_postgres import load_to_postgres


default_args = {
    'start_date': datetime(2024, 1, 1),
    'owner': 'airflow',
    'depends_on_past': False,
    'retries': 0,
}


with DAG(dag_id='meteo_etl_dag',
         description='ETL 6:00 am',
         schedule='0 6 * * *',  #every 6am
         default_args=default_args,
         catchup=False,
         tags=['etl', 'meteo']) as dag:

    """FETCH METEO DATA FROM API"""
    fetch_result = fetch_meteo_data()
    """LOAD GLOBAL METEO DATA as static CSV"""
    historical_data = load_historical_data()
    """FINAL METEO DATA as  CSV"""
    merged_result = clean_and_merged_data(historical_data, fetch_result) #csv + csv file
    """AGGREGATE DAILY DATA"""
    aggregate_result = aggregate_daily(merged_result)  # csv file
    """TRANSFORM TO STAR SCHEMA"""
    transform_result = transform_star_schema(aggregate_result)  # csv file
    """LOAD TO POSTGRES"""
    load_to_postgres_task = load_to_postgres(
        star_schema_dir=transform_result,
        postgres_conn_id="postgres_conn_data"
    )

    fetch_result >> merged_result
    historical_data >> merged_result >> aggregate_result >> transform_result >> load_to_postgres_task

