AIRFLOW_IMAGE_NAME="apache/airflow:3.0.1-python3.12"
_AIRFLOW_WWW_USER_USERNAME=airflow
_AIRFLOW_WWW_USER_PASSWORD=airflow

# The following environment variables are used to configure the Airflow database connection
# AIRFLOW__DATABASE__SQL_ALCHEMY_CONN=sqlite:////opt/airflow/airflow.db
AIRFLOW__DATABASE__SQL_ALCHEMY_CONN=postgresql+psycopg2://airflow:airflow@postgres/airflow

AIRFLOW_UID=50000
AIRFLOW_GID=0
