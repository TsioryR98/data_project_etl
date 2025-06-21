###  folder permission for airflow project and GID 0 only for airflow

sudo chown -R 1000:0 /home/tsioryr/HEI-Etudes/data-airflow/airflow/{dags,logs,plugins,config,scripts,airflow_export}
sudo chmod -R 777 /home/tsioryr/HEI-Etudes/data-airflow/airflow/{dags,logs,plugins,config,scripts,airflow_export}

### folder postgres must be 999:999 
sudo chown -R 999:999 /home/tsioryr/HEI-Etudes/data-airflow/postgres
sudo chmod -R 777 /home/tsioryr/HEI-Etudes/data-airflow/postgres  # 
 (read/write only for postgres)

