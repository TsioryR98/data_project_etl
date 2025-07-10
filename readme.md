
### GITHUB PREPROD BRANCH = main for simulating ETL with docker compose and in dev branch is local execution with python3 venv
# Airflow Project: Weather Data ETL

###  Project structure with docker compose
|__data_airflow
|____airflow
|______|dags/
|______|config/
|______|logs/
|______|plugins/
|_________|scripts/
|____metabase/
|____notebook/

# The images of airflow is made with Dockefile inside airflow directory for manual build from docker Hub registry and requirements.txt for pip install

###  folder permission for airflow project and GID 0 only for airflow
sudo chown -R 1000:0 /home/tsioryr/HEI-Etudes/data-airflow/airflow/{dags,logs,plugins,config,scripts,airflow_export}
sudo chmod -R 777 /home/tsioryr/HEI-Etudes/data-airflow/airflow/{dags,logs,plugins,config,scripts,airflow_export}

### Folder postgres must be 999:999 
sudo chown -R 999:999 /home/tsioryr/HEI-Etudes/data-airflow/postgres
sudo chmod -R 777 /home/tsioryr/HEI-Etudes/data-airflow/postgres  # 
 (read/write only for postgres)



