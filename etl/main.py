from dim_customer import create_dim_customer, insert_dim_customer_data
from dim_order import create_dim_order, insert_dim_order_data
from dim_payment import create_dim_payment, insert_dim_payment_data
from dim_product import create_dim_product, insert_dim_product_data
from dim_review import create_dim_review, insert_dim_review_data
from dim_time import create_dim_time, insert_dim_time_data
from fact_sales import create_fact_sales, insert_fact_sales_data

def main():
    #Creating tables
    create_dim_customer()
    create_dim_order()
    create_dim_payment()
    create_dim_product()
    create_dim_review()
    create_dim_time()
    create_fact_sales()

    #Inserting data into tables
    insert_dim_customer_data()
    insert_dim_order_data()
    insert_dim_payment_data()
    insert_dim_product_data()
    insert_dim_review_data()
    insert_dim_time_data()
    insert_fact_sales_data()


if __name__ == "__main__":
    try:
        main()
        print('Success')
    except Exception as error:
        print(error)
