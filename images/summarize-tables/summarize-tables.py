#!/usr/bin/envpython

import json
import pandas as pd
from sqlalchemy import create_engine

# Create your SQLAlchemy engine
engine = create_engine("mysql://codetest:swordfish@database/codetest")

# Use a connection from the engine
with engine.connect() as connection:
    # Read the table directly into a DataFrame without explicit SQL queries
    df_people = pd.read_sql_table(table_name='people', con=connection)
    df_places = pd.read_sql_table(table_name='places', con=connection)
    result = pd.merge(df_people, df_places, left_on='place_of_birth', right_on='city', how='inner')
    summary = result.groupby('country').size().reset_index(name='count')
    
    # Convert the DataFrame into the desired JSON format
    json_data = dict(zip(summary['country'], summary['count']))

    # Dump the JSON data into a file
    with open('/data/summary_output.json', 'w') as json_file:
        json.dump(json_data, json_file)