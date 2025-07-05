###  folder permission for airflow project and GID 0 only for airflow

sudo chown -R 1000:0 /home/tsioryr/HEI-Etudes/data-airflow/airflow/{dags,logs,plugins,config,scripts,airflow_export}
sudo chmod -R 777 /home/tsioryr/HEI-Etudes/data-airflow/airflow/{dags,logs,plugins,config,scripts,airflow_export}

### Folder postgres must be 999:999 
sudo chown -R 999:999 /home/tsioryr/HEI-Etudes/data-airflow/postgres
sudo chmod -R 777 /home/tsioryr/HEI-Etudes/data-airflow/postgres  # 
 (read/write only for postgres)

| Field               | Description                               | Recommended Final Unit                |
|---------------------|-------------------------------------------|-------------------------------------|
| `location_id`       | Unique city identifier                     | —                                   |
| `city`              | City name                                | —                                   |
| `time` / `timestamp` | Date and time of measurement              | ISO 8601 (e.g., 2025-07-03T21:20:27Z) |
| `temperature`       | Average or instantaneous temperature      | °C                                  |
| `temperature_feel`  | Feels-like temperature                     | °C                                  |
| `apparent_temperature` | Apparent temperature (historical)          | °C                                  |
| `precipitation`     | Total precipitation                        | mm                                  |
| `rain`              | Rain (part of precipitation)               | mm                                  |
| `snow`              | Snowfall (historical)                      | cm                                  |
| `wind_speed`        | Average wind speed                         | km/h (converted from m/s if needed)|
| `cloud_cover` | Cloud coverage (%)                       | %                                   |
| `soil_temperature`  | Soil temperature (historical)              | °C                                  |


### Units in Standard Metric System (°C, km/h, mm, hPa)

# Data Modeling

## Star Schema

### Fact Table: `fact_weather_daily`

| Column               | Description                        |
|----------------------|----------------------------------|
| fact_id (PK)         | Unique identifier for the record |
| location_id (FK)     | Foreign key to `dim_location`    |
| date_id (FK)         | Foreign key to `dim_date`        |
| apparent_temperature | Average apparent temperature     |
| cloud_cover          | Average cloud coverage           |
| precipitation        | Average precipitation            |
| rain                 | Average rain                    |
| snow                 | Average snow                    |
| soil_temperature     | Average soil temperature         |
| temperature          | Average temperature              |
| wind_speed           | Average wind speed               |

### Dimension Tables

#### `dim_location`

| Column         | Description                    |
|----------------|-------------------------------|
| location_id (PK)| Unique identifier of the location |
| city           | City name                     |
| region         | (Optional) Region             |
| country        | (Optional) Country            |
| latitude       | (Optional) Latitude           |
| longitude      | (Optional) Longitude          |

#### `dim_date`

| Column       | Description                   |
|--------------|-------------------------------|
| date_id (PK) | Unique identifier of the date  |
| date         | Date (YYYY-MM-DD)             |
| year         | Year                         |
| month        | Month                        |
| day          | Day                          |
| day_of_week  | Day of the week              |
| quarter      | Quarter                      |

---

## Snowflake Schema

### Fact Table: `fact_weather_daily` (same as star schema)

### Dimension Tables

#### `dim_location`

| Column         | Description                    |
|----------------|-------------------------------|
| location_id (PK)| Unique identifier of the location |
| city           | City name                     |
| region_id (FK) | Foreign key to `dim_region`    |

#### `dim_region`

| Column        | Description                     |
|---------------|--------------------------------|
| region_id (PK)| Unique identifier of the region |
| region_name   | Name of the region              |
| country_id (FK)| Foreign key to `dim_country`    |

#### `dim_country`

| Column        | Description                    |
|---------------|-------------------------------|
| country_id (PK)| Unique identifier of the country |
| country_name  | Name of the country            |

#### `dim_date` (same as star schema)

---

