from datetime import datetime
from utils.constants import default_args

from airflow.sdk import DAG
from airflow.providers.standard.operators.bash import BashOperator

with DAG(
    dag_id="first_dag",
    default_args=default_args,
    description="This is the first dag",
    start_date=datetime(2025, 5, 29),
    schedule="@once"
) as dag:
    task1 = BashOperator(task_id="task1", bash_command="echo Hello world, this is the first task!")
    task2 = BashOperator(task_id="task2", bash_command="echo Hello world, this is the second task!")
    task3 = BashOperator(task_id="task3", bash_command="date")

    task1 >> [task2, task3]

