import sqlite3

connection = sqlite3.connect("data.db")  # create a file- this file is the database

cursor = connection.cursor()

# query

# create table
create_table = "CREATE TABLE IF NOT EXISTS users(id INTEGER PRIMARY KEY, username text, password text)"  # id(auto incremental column) username password
cursor.execute(create_table)

connection.commit()  # necessary if adding any data to database

connection.close()