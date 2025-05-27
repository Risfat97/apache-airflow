from datetime import datetime
from utils.constants import default_args, json_placeholder_baseurl

from airflow import DAG
from airflow.decorators import task
from airflow.providers.http.operators.http import SimpleHttpOperator


def handle_response(response):
    if response.status_code == 200:
        return True
    return False

def handle_data(response):
    print(f"response ===========> {response.json()}")

with DAG(
    dag_id='dag_request_jsonplaceholder',
    default_args=default_args,
    start_date=datetime(2025, 5, 27),
    schedule='@once'
) as dag:
    task1 = SimpleHttpOperator(
        task_id='get_todo_1',
        method='GET',
        http_conn_id='jsonplaceholder',
        endpoint='/todos/1',
        response_check=lambda response: handle_response(response),
        response_filter=lambda response: handle_data(response),
    )