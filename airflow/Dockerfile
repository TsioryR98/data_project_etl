FROM apache/airflow:3.0.2-python3.10

# Installation des paquets système
USER root

RUN apt-get update && \
    apt-get install -y --no-install-recommends build-essential && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Configuration des permissions (sans modifier le GID)
RUN usermod -u 1000 airflow && \
    mkdir -p /opt/airflow && \
    chown -R airflow:0 /opt/airflow && \
    chmod -R g+rwX /opt/airflow

USER airflow
WORKDIR /opt/airflow

COPY --chown=airflow:0 requirements.txt /tmp/requirements.txt
RUN pip install --no-cache-dir -r /tmp/requirements.txt && \
    rm -f /tmp/requirements.txt