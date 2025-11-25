from sqlalchemy import create_engine
from sqlalchemy import text
import pandas as pd

database_name = 'warehouse.db'
engine = create_engine(f'sqlite:///{database_name}')

# This is other way to run the query and see the result
# with engine.connect() as connection:
#     result = connection.execute(text("Select * FROM *"))
#     for row in result:
#         print("", row)

my_query = """
WITH traductions AS (
SELECT
    product_id,
    product_category_name_english,
FROM product_category_name_translation
LEFT JOIN olist_products USING(product_category_name)
),
WITH order_product_price AS (
SELECT 
    olist_orders.order_id,
    olist_orders.customer.id,
    olist_order_items.seller_id,
    olist_order_payments.payment_value,
    olist_orders.order_purchase_timestamp,
    SUM(olist_order_items.price) AS price,
    SUM(olist_order_items.freight_value) AS delivery_price
FROM olist_orders
LEFT JOIN olist_order_payments USING(order_id)
LEFT JOIN olist_order_items USING(order_id)
GROUP BY olist_orders.order_id
)
Select 
    *
FROM
    olist_products
Limit 10
"""

table_1 = pd.read_sql_query(my_query, engine)
print(table_1)