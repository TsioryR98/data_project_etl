from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
from airflow.scripts.meteo_etl_process import fetch_meteo_data

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
    schedule_interval='0 6 * * *',
    schedulel='@daily',
    efault_args=default_args,
    catchup=False,
    tags=['etl', 'meteo']
) as dag :
    etl_task = PythonOperator(
        task_id='fetch_meteo_data',
        python_callable=fetch_meteo_data
    )