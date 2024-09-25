CREATE TABLE dim_order (                          				--Creating dim_order
	order_id						VARCHAR(50) PRIMARY KEY,
	order_status					VARCHAR(20),
	price							DECIMAL(10, 2),
	freight_value					DECIMAL(10, 2)
);

CREATE TABLE dim_customer (                          				--Creating dim_customer
	customer_unique_id				VARCHAR(50) PRIMARY KEY,
	customer_id						VARCHAR(50),
	customer_zip_code_prefix		INT,
	customer_city   				VARCHAR(40),
	customer_state     				CHAR(2)
);

CREATE TABLE dim_product (                          				--Creating dim_product
	product_id						VARCHAR(50) PRIMARY KEY,
	product_category_name			VARCHAR(50),
	product_name_lenght				INT,
	product_description_lenght		INT,
	product_photos_qty				INT,
	product_weight_g				INT,
	product_lenght_cm				INT,
	product_height_cm				INT,
	product_width_cm				INT
);

CREATE TABLE dim_payment (                          				--Creating dim_payment
	order_id						VARCHAR(50) PRIMARY KEY,
	payment_sequential				INT,
	payment_type					VARCHAR(20),
	payment_installments			INT,
	payment_value					DECIMAL(10, 2)
);

CREATE TABLE dim_review (                          				--Creating dim_review
	review_id						VARCHAR(50) PRIMARY KEY,
	review_score					INT,
	review_comment_title			VARCHAR(50),
	review_comment_message			VARCHAR(255)
);

CREATE TABLE dim_time (                          					--Creating dim_time
	order_id						VARCHAR(50) PRIMARY KEY,
	order_purchase_timestamp		TIMESTAMP,
	order_approved_at				TIMESTAMP,
	order_delivered_carrier_date 	TIMESTAMP,
	order_delivered_customer_date 	TIMESTAMP,
	order_estimated_delivery_date 	TIMESTAMP,
	shipping_limit_date				TIMESTAMP,
	review_creation_date			TIMESTAMP,
	review_answer_timestamp			TIMESTAMP
);

CREATE TABLE fact_sale (                          				--Creating fact_sale
	sale_id							SERIAL PRIMARY KEY,
	seller_id						VARCHAR(50),
	order_id						VARCHAR(50),
	order_item_id					INT,
	customer_id						VARCHAR(50),
	product_id						VARCHAR(50),
	review_id						VARCHAR(50),
	FOREIGN KEY (order_id) REFERENCES dim_order(order_id),
	FOREIGN KEY (order_id) REFERENCES dim_payment(order_id),
	FOREIGN KEY (order_id) REFERENCES dim_time(order_id),
	FOREIGN KEY (customer_id) REFERENCES dim_customer(customer_id),
	FOREIGN KEY (product_id) REFERENCES dim_product(product_id),
	FOREIGN KEY (review_id) REFERENCES dim_review(review_id)
);
