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
Select 
    *
FROM
    product_category_name_translation
Limit 10
"""
table_1 = pd.read_sql_query(my_query, engine)
print(table_1)