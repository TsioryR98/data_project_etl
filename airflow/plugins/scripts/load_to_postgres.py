import os
from airflow.decorators import task
from airflow.providers.postgres.hooks.postgres import PostgresHook

@task
def load_to_postgres(star_schema_dir: str, postgres_conn_id: str) -> None:
    """
    COPY (psycopg2).
    """
    hook = PostgresHook(postgres_conn_id=postgres_conn_id)
    conn = hook.get_conn()
    cur  = conn.cursor()

    files = {
        "dim_location": os.path.join(star_schema_dir, "dim_location.csv"),
        "dim_time":     os.path.join(star_schema_dir, "dim_time.csv"),
        "fact_weather": os.path.join(star_schema_dir, "fact_weather.csv"),
    }

    for table, path in files.items():
        with open(path, "r", encoding="utf-8") as f:
            cur.copy_expert(
                sql=f"COPY {table} FROM STDIN WITH CSV HEADER",
                file=f
            )
        conn.commit()

    cur.close()
    conn.close()
