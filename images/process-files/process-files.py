#!/usr/bin/envpython
   
import pandas as pd
from sqlalchemy import create_engine

# Read the CSV file into a DataFrame
df_places = pd.read_csv('/data/places.csv')
df_people = pd.read_csv('/data/people.csv')

# Create your SQLAlchemy engine
engine = create_engine("mysql://codetest:swordfish@database/codetest")

# Insert DataFrame into MySQL table
place_table = 'places'
people_table = 'people'

# Use a connection from the engine
with engine.connect() as connection:
    df_places.to_sql(name=place_table, con=connection, if_exists='append', index=False)
    df_people.to_sql(name=people_table, con=connection, if_exists='append', index=False)