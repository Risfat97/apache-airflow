from datetime import datetime
from utils.constants import default_args

from airflow import DAG
from airflow.decorators import task

@task(task_id='greeting')
def greeting(who="World"):
    print(f"Hello {who}!")

@task(task_id='print_context')
def print_context(ds=None, **kwargs):
    print(kwargs)
    print(ds)
    return 0

with DAG(
    dag_id="first_dag_with_python_op",
    default_args=default_args,
    description="This is our the first dag with Python operator",
    start_date=datetime(2025, 5, 27),
    schedule="@once"
) as dag:
    task1 = greeting(who="Sirtaf")
    task2 = print_context()

    task1 >> task2