import pandas as pd
from db_conection import get_connection

#Creating dim_review
def create_dim_review():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('''
                CREATE TABLE IF NOT EXISTS dim_review (
                review_id						VARCHAR(50) PRIMARY KEY,
                review_score					INT,
                review_comment_title			VARCHAR(50),
                review_comment_message			VARCHAR(255))
''')
    conn.commit()
    cursor.close()
    conn.close()

#Inserting data from order_reviews_df into dim_review
def insert_dim_review_data():
    conn = get_connection()
    cursor = conn.cursor()
    #Loading order_reviews_dataset.csv data
    order_reviews_df = pd.read_csv('C://Users/Main/Projetos/desafio-i/dataset/olist_order_reviews_dataset.csv')
    #Creating review_df
    review_df = pd.DataFrame({
            'review_id' : order_reviews_df ['review_id'],
            'review_score' : order_reviews_df ['review_score'],
            'review_comment_title' : order_reviews_df ['review_comment_title'],
            'review_comment_message' : order_reviews_df ['review_comment_message']
    })
    review_df = review_df.drop_duplicates()
    review_df['review_comment_title'] = review_df['review_comment_title'].fillna('Título da avaliação')
    review_df['review_comment_message'] = review_df['review_comment_message'].fillna('Sem mensagem de avaliação')
    #Inserting data into dim_review
    for index, row in review_df.iterrows():
        cursor.execute('INSERT INTO dim_review (review_id, review_score, review_comment_title, review_comment_message) VALUES (%s, %s, %s, %s)', (row.review_id, row.review_score, row.review_comment_title, row.review_comment_message))
    conn.commit()
    cursor.close()
    conn.close()
