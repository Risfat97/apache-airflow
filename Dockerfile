FROM apache/airflow:3.0.1-python3.12

COPY --chown=airflow:root ./dags/ /opt/airflow/dags/

# (Optionnal) Copy plugins if needed
# COPY --chown=airflow:root ./plugins/ /opt/airflow/plugins/

# (Optionnal) Install additionnal Python packages
# COPY requirements.txt .
# RUN pip install --no-cache-dir -r requirements.txt