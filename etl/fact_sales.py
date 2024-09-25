import pandas as pd
from db_conection import get_connection

#Creating fact_sales
def create_fact_sales():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('''
                CREATE TABLE IF NOT EXISTS fact_sales (
                sale_id							SERIAL PRIMARY KEY,
                order_id						VARCHAR(50),
                order_item_id					INT,
                seller_id						VARCHAR(50),
                customer_unique_id				VARCHAR(50),
                product_id						VARCHAR(50),
                review_id						VARCHAR(50),
                FOREIGN KEY (order_id) REFERENCES dim_order(order_id),
                FOREIGN KEY (order_id) REFERENCES dim_payment(order_id),
                FOREIGN KEY (order_id) REFERENCES dim_time(order_id),
                FOREIGN KEY (customer_unique_id) REFERENCES dim_customer(customer_unique_id),
                FOREIGN KEY (product_id) REFERENCES dim_product(product_id),
                FOREIGN KEY (review_id) REFERENCES dim_review(review_id))
''')
    conn.commit()
    cursor.close()
    conn.close()

#Inserting data from orders_df, customers_df, payments_df, products_df, order_reviews_df into fact_sales
def insert_fact_sales_data():
    conn = get_connection()
    cursor = conn.cursor()
    #Loading orders_dataset.csv data
    orders_df = pd.read_csv('C://Users/Main/Projetos/desafio-i/dataset/olist_orders_dataset.csv')
    #Loading order_items_dataset.csv data
    order_items_df = pd.read_csv('C://Users/Main/Projetos/desafio-i/dataset/olist_order_items_dataset.csv')
    #Loading customers_dataset.csv data
    customers_df = pd.read_csv('C://Users/Main/Projetos/desafio-i/dataset/olist_customers_dataset.csv')
    #Loading products_dataset.csv data
    products_df = pd.read_csv('C://Users/Main/Projetos/desafio-i/dataset/olist_products_dataset.csv')
    #Loading order_reviews_dataset.csv data
    order_reviews_df = pd.read_csv('C://Users/Main/Projetos/desafio-i/dataset/olist_order_reviews_dataset.csv')
    #Creating order_df
    sales_df = pd.DataFrame({
        'order_id' : order_items_df ['order_id'],
        'order_item_id' : order_items_df ['order_item_id'],
        'seller_id' : order_items_df ['seller_id'],
        'customer_unique_id' : customers_df['customer_unique_id'],
        'product_id' : products_df ['product_id'],
        'review_id' : order_reviews_df ['review_id'],
        'price' : order_items_df ['price'],
        'freight_value' : order_items_df ['freight_value'],
        'review_score' : order_reviews_df ['review_score']
    })
    #Inserting data into fact_sales
    for index, row in sales_df.iterrows():
        cursor.execute('INSERT INTO fact_sales (order_id, order_item_id, seller_id, customer_unique_id, product_id, review_id, price, freight_value, review_score) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)', (row.order_id, row.order_item_id, row.seller_id, row.customer_unique_id, row.product_id, row.review_id, row.price, row.freight_value, row.review_score))
    conn.commit()
    cursor.close()
    conn.close()
