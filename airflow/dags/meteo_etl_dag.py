from airflow import DAG
from datetime import datetime, timedelta
import sys
sys.path.insert(0, '/opt/airflow')
from plugins.scripts.meteo_etl_process import fetch_meteo_data
from airflow.decorators import task

default_args = {
    'start_date': datetime(2024, 1, 1),
    'owner': 'airflow',
    'depends_on_past': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

with DAG(
    dag_id='meteo_etl_dag',
    description='ETL 6:00 am',
    schedule='*/5 * * * *',
    default_args=default_args,
    catchup=False,
    tags=['etl', 'meteo']
) as dag :
    """FETCH METEO DATA FROM API"""
    fetch_task = task(fetch_meteo_data)()
