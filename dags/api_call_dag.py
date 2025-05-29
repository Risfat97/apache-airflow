import logging
from datetime import datetime
from utils.constants import default_args

from airflow.sdk import DAG
from airflow.decorators import task
from airflow.providers.standard.operators.empty import EmptyOperator
from airflow.providers.http.operators.http import HttpOperator


def check_response(response):
    if response.status_code == 200:
        return True
    return False

def handle_data(response):
    logging.info(f"Response ===========> {response.json()}")

with DAG(
    dag_id='get_todos',
    default_args=default_args,
    description='This is a dag to perform API calls with HTTP operator',
    start_date=datetime(2025, 5, 29),
    schedule='@once'
) as dag:
    first = EmptyOperator(task_id="start")
    end = EmptyOperator(task_id="end")

    for i in range(1, 3):
        task = HttpOperator(
            task_id=f"get_todo{i}",
            endpoint=f"/todos/{i}",
            method="GET",
            http_conn_id="jsonplaceholder_api",
            headers={"Content-Type": "application/json"},
            response_check=lambda response: check_response(response),
            response_filter=lambda response: handle_data(response)
        )
        first >> task >> end