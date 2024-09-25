import psycopg2

database = 'olist-dw'
host = 'localhost'
user = 'postgres'
pwd = 'w#UAC7EaiV8itkBG4L4rd6%jE!fBgQ'
port_id = '5432'

#Establishing a connection with postgreSQL

def get_connection():
    conn = psycopg2.connect(
        database = database, 
        host = host,
        user = user,
        password = pwd,
        port = port_id)
    return conn
