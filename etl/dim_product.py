import pandas as pd
from db_conection import get_connection

#Creating dim_product
def create_dim_product():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('''
                CREATE TABLE IF NOT EXISTS dim_product (
                product_id						VARCHAR(50) PRIMARY KEY,
                product_category_name			VARCHAR(50),
                product_name_lenght				INT,
                product_description_lenght		INT,
                product_photos_qty				INT,
                product_weight_g				INT,
                product_length_cm				INT,
                product_height_cm				INT,
                product_width_cm				INT)
''')
    conn.commit()
    cursor.close()
    conn.close()

#Inserting data from products_df into dim_product
def insert_dim_product_data():
    conn = get_connection()
    cursor = conn.cursor()
    #Loading products_dataset.csv data
    products_df = pd.read_csv('C://Users/Main/Projetos/desafio-i/dataset/olist_products_dataset.csv')
    products_df['product_category_name'] = products_df['product_category_name'].fillna('Outro')
    numeric_cols = products_df.select_dtypes(include=['float64', 'int64']).columns
    products_df[numeric_cols] = products_df[numeric_cols].fillna(products_df[numeric_cols].mean())
    #Inserting data into dim_product
    for index, row in products_df.iterrows():
        cursor.execute('INSERT INTO dim_product (product_id, product_category_name, product_name_lenght, product_description_lenght, product_photos_qty, product_weight_g, product_length_cm, product_height_cm, product_width_cm) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)', (row.product_id, row.product_category_name, row.product_name_lenght, row.product_description_lenght, row.product_photos_qty, row.product_weight_g, row.product_length_cm, row.product_height_cm, row.product_width_cm))
    conn.commit()
    cursor.close()
    conn.close()
    