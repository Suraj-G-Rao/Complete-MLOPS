"""
Apache Airflow introduced the TaskFlow API which allows you to create tasks 
using Python decorators like @task. This is a cleaner and more intuitive way 
of writing tasks without needing to manually use operators like PythonOperator.
Let me show you how to modify the previous code to use the @task decorator.
"""

from airflow import DAG
from airflow.decorators import task
from datetime import datetime

## Define the DAG

with DAG(
    dag_id='math_sequence_dag_with_taskflow',
    start_date=datetime(2023,1,1),
    schedule_interval='@once',
    catchup=False,
) as dag:
    

    # Task 1: Start With the initial number
    @task
    def start_number():
        initial_value=10
        print(f"Starting number: {initial_value}")
        return initial_value
    
    # Task 2: Add 5 to the number
    @task
    def add_five(number):
        new_value = number + 5
        print(f"Add 5: {number} + 5 = {new_value}")
        return new_value
    
    # Task 3: Multiply by 2
    @task
    def multiply_by_two(number):
        new_value = number * 2
        print(f"Multiply by 2: {number} * 2 = {new_value}")
        return new_value
    
     # Task 4: Subtract 3
    @task
    def subtract_three(number):
        new_value = number - 3
        print(f"Subtract 3: {number} - 3 = {new_value}")
        return new_value
    
    # Task 5: Square the number
    @task
    def square_number(number):
        new_value = number ** 2
        print(f"Square the result: {number}^2 = {new_value}")
        return new_value
    
    ## Set task dependencies
    start_value=start_number()
    added_values=add_five(start_value)
    multiplied_value=multiply_by_two(added_values)
    subtracted_value=subtract_three(multiplied_value)
    square_value=square_number(subtracted_value)
