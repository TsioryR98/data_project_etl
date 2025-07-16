CREATE TABLE IF NOT EXISTS dim_location (
    location_id INTEGER PRIMARY KEY,
    city VARCHAR(50)
);


CREATE TABLE IF NOT EXISTS fact_weather (
    location_id INTEGER,
    date_id INTEGER,
    apparent_temperature FLOAT,
    cloud_cover FLOAT,
    precipitation FLOAT,
    rain FLOAT,
    snow FLOAT,
    soil_temperature FLOAT,
    temperature FLOAT,
    wind_speed FLOAT,
    PRIMARY KEY (location_id, date_id),
    FOREIGN KEY (location_id) REFERENCES dim_location(location_id),
    FOREIGN KEY (date_id) REFERENCES dim_time(date_id)
);

CREATE TABLE IF NOT EXISTS dim_time (
    date DATE,
    date_id INTEGER PRIMARY KEY,
    year INTEGER,
    month INTEGER,
    day INTEGER,
    day_of_week INTEGER,
    quarter INTEGER
);

