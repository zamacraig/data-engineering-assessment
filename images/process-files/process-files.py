#!/usr/bin/envpython

import csv
import sqlalchemy

# connect to the database
engine = sqlalchemy.create_engine("mysql://codetest:swordfish@database/codetest")
connection = engine.connect()

metadata = sqlalchemy.schema.MetaData(engine)

people = sqlalchemy.schema.Table('people', metadata, autoload=True, autoload_with=engine)

places = sqlalchemy.schema.Table('places', metadata, autoload=True, autoload_with=engine)

# read the CSV data file into the table
with open('/data/places.csv') as csv_file:
  reader = csv.reader(csv_file)
  next(reader)
  for row in reader: 
    connection.execute(places.insert().values(city = row[0], county = row[1], country = row[2]))
    
# read the CSV data file into the table
with open('/data/people.csv') as csv_file:
  reader = csv.reader(csv_file)
  next(reader)
  for row in reader: 
    connection.execute(people.insert().values(given_name = row[0], family_name = row[1], date_of_birth = row[2], place_of_birth = row[3]))