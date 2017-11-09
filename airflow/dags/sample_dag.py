from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from datetime import datetime, timedelta

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(year=2017, month=11, day=9, hour=17),
    'retries': 1,
    'retry_delay': timedelta(minutes=4)
}

dag = DAG('sample_dag', default_args=default_args, schedule_interval=timedelta(minutes=10))

t1 = BashOperator(
    task_id='print_hello',
    bash_command='echo "hello"',
    dag=dag)