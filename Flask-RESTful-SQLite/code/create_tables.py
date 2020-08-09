import sqlite3

connection = sqlite3.connect("data.db")  # create a file- this file is the database

cursor = connection.cursor()

# query

# create table
create_table = "CREATE TABLE IF NOT EXISTS users(id INTEGER PRIMARY KEY, username text, password text)"  # id(auto incremental column) username password
cursor.execute(create_table)

# create another table
create_table = "CREATE TABLE IF NOT EXISTS items(name text, price real)"
cursor.execute(create_table)
cursor.execute("INSERT INTO items VALUES ('test', 999.99)")


connection.commit()  # necessary if adding any data to database

connection.close()