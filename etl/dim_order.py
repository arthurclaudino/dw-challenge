import pandas as pd
from db_conection import get_connection

#Creating dim_order
def create_dim_order():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('''
                CREATE TABLE IF NOT EXISTS dim_order (
                order_id						VARCHAR(50) PRIMARY KEY,
                order_status					VARCHAR(20),
                price							DECIMAL(10, 2),
                freight_value					DECIMAL(10, 2))
''')
    conn.commit()
    cursor.close()
    conn.close()

#Inserting data from orders_df into dim_order
def insert_dim_order_data():
    conn = get_connection()
    cursor = conn.cursor()
    #Loading orders_dataset.csv data
    orders_df = pd.read_csv('C://Users/Main/Projetos/desafio-i/dataset/olist_orders_dataset.csv')
    #Loading order_items_dataset.csv data
    order_items_df = pd.read_csv('C://Users/Main/Projetos/desafio-i/dataset/olist_order_items_dataset.csv')
    #Creating order_df
    order_df = pd.DataFrame({
            'order_id' : order_items_df ['order_id'],
            'order_status' : orders_df ['order_status'],
            'price' : order_items_df ['price'],
            'freight_value' : order_items_df ['freight_value']
        })
    order_df = order_df.dropna(how="any")
    order_df = order_df.drop_duplicates(subset='order_id', keep='first')
    #Inserting data from orders_df into dim_order
    for index, row in order_df.iterrows():
        cursor.execute('INSERT INTO dim_order (order_id, order_status, price, freight_value) VALUES (%s, %s, %s, %s)', (row.order_id, row.order_status, row.price, row.freight_value))
    conn.commit()
    cursor.close()
    conn.close()
