###  folder permission for airflow project and GID 0 only for airflow

sudo chown -R 1000:0 /home/tsioryr/HEI-Etudes/data-airflow/airflow/{dags,logs,plugins,config}
sudo chmod -R 777 /home/tsioryr/HEI-Etudes/data-airflow/airflow/{dags,logs,plugins,config}

### folder postgres must be 999:999 
sudo chown -R 999:0 /home/tsioryr/HEI-Etudes/data-airflow/postgres_data
sudo chmod -R 777 /home/tsioryr/HEI-Etudes/data-airflow/postgres_data  # Temporairement permissif
 (read/write only for postgres)

