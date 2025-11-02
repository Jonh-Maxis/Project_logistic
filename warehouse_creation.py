# --- 1. IMPORTS ---
import pandas as pd
import os 
from sqlalchemy import create_engine

# --- 2. CONFIGURATION ---
# Define database file name and connection string
database_name = 'warehouse.db'
engine = create_engine(f'sqlite:///{database_name}')
csv_directory = 'data/archive'
lecture = os.listdir(csv_directory)

# --- 3. ETL (EXTRACT, TRANSFORM, LOAD) ---
# Loop through each file in the source directory.
# For each file: Read it into Pandas, clean the table name,
# and write it to a new table in the SQLite database.
print("starting data load... ")
for file_name in lecture:
   # EXTRACT (from CSV)
   archivo = os.path.join(csv_directory,file_name)
   read_pdf = pd.read_csv(archivo)
   # TRANSFORM (Table name)
   file_name = file_name.replace('.csv','').replace('_dataset','')
   # LOAD 
   read_pdf.to_sql(
      name=file_name,
      con=engine,
      if_exists='replace',
      index=False
   )
   print(f"Succesfully loaded {file_name} ({len(read_pdf)} rows)")

print("Database load complete")

