import sqlite3


class ItemModel:
    def __init__(self, name, price):  # later be used either inserted or updated to database
        self.name = name
        self.price = price

    def json(self):
        return { "name": self.name, "price": self.price }

    @classmethod
    def find_by_name(cls, name):  # !this is going to return an object
        connection = sqlite3.connect("data.db")
        cursor = connection.cursor()

        query = "SELECT * FROM items WHERE name=?"
        result = cursor.execute(query, (name,))
        row = result.fetchone()

        connection.close()

        if row:
            item_json = ItemModel.json(cls(*row))  # row[0], row[1]
            return {"item": item_json}

    def insert(self):  # !this is not going to return anything-create object instance-item.insert()
        connection = sqlite3.connect("data.db")
        cursor = connection.cursor()

        insert_query = "INSERT INTO items VALUES(?, ?)"
        cursor.execute(insert_query, (self.name, self.price))

        connection.commit()  # need to commit!
        connection.close()

    def update(self):
        connection = sqlite3.connect("data.db")
        cursor = connection.cursor()

        update_query = "UPDATE FROM items SET price=? WHERE  name=?"
        cursor.execute(update_query, (self.price, self.name))

        connection.commit()  # need to commit!
        connection.close()
