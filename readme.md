###  folder permission for airflow project and GID 0 only for airflow

sudo chown -R 1000:0 /home/tsioryr/HEI-Etudes/data-airflow/airflow/{dags,logs,plugins,config,scripts,airflow_export}
sudo chmod -R 777 /home/tsioryr/HEI-Etudes/data-airflow/airflow/{dags,logs,plugins,config,scripts,airflow_export}

### Folder postgres must be 999:999 
sudo chown -R 999:999 /home/tsioryr/HEI-Etudes/data-airflow/postgres
sudo chmod -R 777 /home/tsioryr/HEI-Etudes/data-airflow/postgres  # 
 (read/write only for postgres)

| Champ                        | Description                              | Unité finale recommandée             |
|------------------------------|------------------------------------------|---------------------------------------|
| `location_id`                | Identifiant unique de la ville           | —                                    |
| `ville`                      | Nom de la ville                          | —                                    |
| `time` / `timestamp`         | Date et heure de la mesure               | ISO 8601 (ex: 2025-07-03T21:20:27Z) |
| `temperature`                | Température moyenne ou instantanée       | °C                                   |
| `temperature_max`            | Température maximale                     | °C                                   |
| `temperature_min`            | Température minimale                     | °C                                   |
| `temperature_feel`           | Température ressentie                    | °C                                   |
| `apparent_temperature`       | Température apparente (historique)       | °C                                   |
| `precipitation`              | Précipitations totales                   | mm                                   |
| `rain`                       | Pluie (partie de précipitations)         | mm                                   |
| `snowfall`                   | Chute de neige (historique)              | cm                                   |
| `rain_day`                   | Quantité pluie journalière (OpenWeather) | mm                                   |
| `weather_code`               | Code météo (ex: WMO)                     | — (code numérique ou catégorie)      |
| `weather`                    | Description météo (ex: Clear, Rain)      | —                                    |
| `humidity`                   | Humidité relative                        | %                                    |
| `pression`                   | Pression atmosphérique                   | hPa                                  |
| `wind_speed`                 | Vitesse moyenne du vent                  | km/h (converti depuis m/s si besoin) |
| `wind_gusts`                 | Rafales de vent (historique)             | km/h                                 |
| `cloud_cover` / `cloud_rate` | Couverture nuageuse (%)                  | %                                    |
| `soil_temperature`           | Température du sol (historique)          | °C                                   |



###  Les unités en Système métrique standard (°C, km/h, mm, hPa)