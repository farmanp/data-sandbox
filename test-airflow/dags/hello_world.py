from datetime import datetime, timedelta

from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.operators.python_operator import PythonOperator

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2022, 1, 1),
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}


dag = DAG(
    'hello_world',
    default_args=default_args,
    description='A simple DAG that prints "Hello, World!"',
    schedule_interval=timedelta(days=1),
    catchup=False,
)

def print_hello():
    print('Hello, World!')

print_hello_task = PythonOperator(
    task_id='print_hello_task',
    python_callable=print_hello,
    dag=dag,
)

echo_hello_task = BashOperator(
    task_id='echo_hello_task',
    bash_command='echo "Hello, World!" >> /usr/local/airflow/hello_world.txt',
    dag=dag,
)

print_hello_task >> echo_hello_task
