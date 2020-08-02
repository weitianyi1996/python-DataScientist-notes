import sqlite3

connection = sqlite3.connect("data.db")  # create a file- this file is the database

cursor = connection.cursor()

# query

# create table
create_table = "CREATE TABLE users(id int, username text, password text)"  # id username password
cursor.execute(create_table)

# insert values to table
user = (1, "Toby", "password123")
insert_query = "INSERT INTO users VALUES(?,?,?)"
cursor.execute(insert_query, user)

users = [
    (2, "Aoby", "password233"),
    (1, "Boby", "password323")
]
cursor.executemany(insert_query, users)

# SQL
select_query = "SELECT* FROM users"
for row in cursor.execute(select_query):
    print(row)

connection.commit()

connection.close()


