import pandas as pd
from db_conection import get_connection

#Creating dim_time
def create_dim_time():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('''
                CREATE TABLE IF NOT EXISTS dim_time (
                order_id						VARCHAR(50) PRIMARY KEY,
                order_purchase_timestamp		TIMESTAMP,
                order_approved_at				TIMESTAMP,
                order_delivered_carrier_date 	TIMESTAMP,
                order_delivered_customer_date 	TIMESTAMP,
                order_estimated_delivery_date 	TIMESTAMP,
                shipping_limit_date				TIMESTAMP,
                review_creation_date			TIMESTAMP,
                review_answer_timestamp			TIMESTAMP)
''')
    conn.commit()
    cursor.close()
    conn.close()

#Inserting data from orders_df, order_items_df, order_reviews_df into dim_time
def insert_dim_time_data():
    conn = get_connection()
    cursor = conn.cursor()
    #Loading orders_dataset.csv data
    orders_df = pd.read_csv('C://Users/Main/Projetos/desafio-i/dataset/olist_orders_dataset.csv')
    #Loading order_items_dataset.csv data
    order_items_df = pd.read_csv('C://Users/Main/Projetos/desafio-i/dataset/olist_order_items_dataset.csv')
    #Loading order_reviews_dataset.csv data
    order_reviews_df = pd.read_csv('C://Users/Main/Projetos/desafio-i/dataset/olist_order_reviews_dataset.csv')
    #Creating time_df
    time_df = pd.DataFrame({
            'order_id' : orders_df ['order_id'],
            'order_purchase_timestamp' : orders_df ['order_purchase_timestamp'],
            'order_approved_at' : orders_df ['order_approved_at'],
            'order_delivered_carrier_date' : orders_df ['order_delivered_carrier_date'],
            'order_delivered_customer_date' : orders_df ['order_delivered_customer_date'],
            'order_estimated_delivery_date' : orders_df ['order_estimated_delivery_date'],
            'shipping_limit_date' : order_items_df ['shipping_limit_date'],
            'review_creation_date' : order_reviews_df ['review_creation_date'],
            'review_answer_timestamp' : order_reviews_df ['review_answer_timestamp']
    })
    time_df = time_df.dropna(how="any")
    #Inserting data into dim_time
    for index, row in time_df.iterrows():
        cursor.execute('INSERT INTO dim_time (order_id, order_purchase_timestamp, order_approved_at, order_delivered_carrier_date, order_delivered_customer_date, order_estimated_delivery_date, shipping_limit_date, review_creation_date, review_answer_timestamp) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)', (row.order_id, row.order_purchase_timestamp, row.order_approved_at, row.order_delivered_carrier_date, row.order_delivered_customer_date, row.order_estimated_delivery_date, row.shipping_limit_date, row.review_creation_date, row.review_answer_timestamp,))
    conn.commit()
    cursor.close()
    conn.close()
