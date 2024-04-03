# Import libraries yang dibutuhkan
import datetime as dt
from datetime import timedelta
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
import pandas as pd

def data_cleaning():
    data=pd.read_csv('/opt/airflow/dags/properties_data.csv')
    data=data.drop_duplicates()
    data=data.dropna()
    data = data.drop(['id', 'latitude', 'longitude'], axis=1)
    final_column = ['neighborhood','price','size_in_sqft','price_per_sqft','no_of_bedrooms','no_of_bathrooms',
                    'maid_room','concierge','pets_allowed','private_garden','private_gym','private_jacuzzi','private_pool','shared_pool']
    data = data[final_column]
    data.to_csv('/opt/airflow/dags/properties_data_clean.csv')
    
default_args = {
'owner': 'sandy',
'start_date': dt.datetime(2024, 4, 2),
'retries': 1,
'retry_delay': dt.timedelta(minutes=1),
}

with DAG('Final_Project',
         default_args=default_args,
         schedule_interval='48 7 * * *',
         ) as dag:

    clean_data = PythonOperator(task_id='data_cleaning_and_transform_to_.csv', python_callable=data_cleaning)

clean_data 