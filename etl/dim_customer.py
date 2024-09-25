import pandas as pd
from db_conection import get_connection

#Creating dim_customer
def create_dim_customer():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('''
                CREATE TABLE IF NOT EXISTS dim_customer (
                customer_unique_id				VARCHAR(50) PRIMARY KEY,
                customer_id				        VARCHAR(50),
                customer_zip_code_prefix		INT,
                customer_city   				VARCHAR(40),
                customer_state     				CHAR(2))
''')
    conn.commit()
    cursor.close()
    conn.close()

#Inserting data from customers_df into dim_customer
def insert_dim_customer_data():
    conn = get_connection()
    cursor = conn.cursor()
    #Loading customers_dataset.csv data
    customers_df = pd.read_csv('C://Users/Main/Projetos/desafio-i/dataset/olist_customers_dataset.csv')
    customers_df = customers_df.drop_duplicates(subset='customer_unique_id')
    #Inserting data into dim_customer
    for index, row in customers_df.iterrows():
        cursor.execute('INSERT INTO dim_customer (customer_unique_id, customer_id, customer_zip_code_prefix, customer_city, customer_state) VALUES (%s, %s, %s, %s, %s)', (row.customer_unique_id, row.customer_id, row.customer_zip_code_prefix, row.customer_city, row.customer_state))
    conn.commit()
    cursor.close()
    conn.close()
