# Airflow Project: Weather Data ETL

### GITHUB BRANCHES
- **PREPROD BRANCH (main)** : ETL simulation with docker compose
- **DEV BRANCH** : Local execution with python3 venv

### PROJECT STRUCTURE (DOCKER COMPOSE VERSION)

data_airflow/
├── airflow/
│ ├── dags/ # Airflow DAG files
│ ├── config/ # Configuration files
│ ├── logs/ # Execution logs
│ ├── plugins/
│ │ └── scripts/ # Custom scripts
├── metabase/ # Metabase configuration
├── notebook/ # Jupyter notebooks
├── postgres/ # PostgreSQL data


## Docker Setup
- Custom Airflow image built from Dockerfile
- Based on official Docker Hub registry image
- Python dependencies in requirements.txt

## Folder Permissions
```bash
# Airflow directories (UID 1000, GID 0)
sudo chown -R 1000:0 ./airflow/{dags,logs,plugins,config,scripts,airflow_export}
sudo chmod -R 777 ./airflow/{dags,logs,plugins,config,scripts,airflow_export}

# PostgreSQL directory (UID/GID 999)
sudo chown -R 999:999 ./postgres
sudo chmod -R 777 ./postgres

```
