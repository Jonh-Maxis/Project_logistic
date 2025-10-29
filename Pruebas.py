
import pandas as pd
import os 
from sqlalchemy import create_engine

database_name = 'warehouse.db'
engine = create_engine(f'sqlite:///{database_name}')
csv_directory = 'data/archive'
lecture = os.listdir(csv_directory)

for file_name in lecture:
   archivo = os.path.join(csv_directory,file_name)
   read_pdf = pd.read_csv(archivo)
   file_name = file_name.replace('.csv','').replace('_dataset','')
   read_pdf.to_sql(
      name=file_name,
      con=engine,
      if_exists='replace',
      index=False)
