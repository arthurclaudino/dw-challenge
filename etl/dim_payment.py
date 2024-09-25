import pandas as pd
from db_conection import get_connection

#Creating dim_payment
def create_dim_payment():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('''
                CREATE TABLE IF NOT EXISTS dim_payment (
                order_id						VARCHAR(50) PRIMARY KEY,
                payment_sequential				INT,
                payment_type					VARCHAR(20),
                payment_installments			INT,
                payment_value					DECIMAL(10, 2))
''')
    conn.commit()
    cursor.close()
    conn.close()

#Inserting data from payments_df into dim_payment
def insert_dim_payment_data():
    conn = get_connection()
    cursor = conn.cursor()
    #Loading order_payments_dataset.csv data
    payments_df = pd.read_csv('C://Users/Main/Projetos/desafio-i/dataset/olist_order_payments_dataset.csv')
    payments_df = payments_df.drop_duplicates(subset='order_id')
    #Inserting data into dim_payment
    for index, row in payments_df.iterrows():
        cursor.execute('INSERT INTO dim_payment (order_id, payment_sequential, payment_type, payment_installments, payment_value) VALUES (%s, %s, %s, %s, %s)', (row.order_id, row.payment_sequential, row.payment_type, row.payment_installments, row.payment_value))
    conn.commit()
    cursor.close()
    conn.close()
