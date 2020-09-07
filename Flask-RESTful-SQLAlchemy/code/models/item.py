# import sqlite3
from db import db


class ItemModel(db.Model):
    __tablename__ = "items"

    # 3 columns SQLAlchemt must match instance properties(self.id, username, password)
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    price = db.Column(db.Float(precision=2))
    store_id = db.Column(db.Integer, db.Foreignkey("stores.id"))
    store = db.relationship("StoreModel")

    def __init__(self, name, price, store_id):  # later be used either inserted or updated to database
        self.name = name
        self.price = price
        self.store_id = store_id

    def json(self):
        return {"name": self.name, "price": self.price}

    @classmethod
    def find_by_name(cls, name):  # !this is going to return an object
        # connection = sqlite3.connect("data.db")
        # cursor = connection.cursor()
        #
        # query = "SELECT * FROM items WHERE name=?"
        # result = cursor.execute(query, (name,))
        # row = result.fetchone()
        #
        # connection.close()
        #
        # if row:
        #     item_json = ItemModel.json(cls(*row))  # row[0], row[1]
        #     return {"item": item_json}

        # using SQLAlchemy-difference: SQLite using SQL(SELECT*FROM A), SQLAlchemy using query/filter...
        # return an ItemModel object(because of cls)
        # row in db -transformed to- class object with properties(self.name, self.price)
        item_json = cls.query.filter_by(name=name).first().json()  # SELECT*FROM items WHERE name=name LIMIT 1
        return {"item": item_json}

    def save_to_db(self):  # !this is not going to return anything-create object instance-item.insert()
        # connection = sqlite3.connect("data.db")
        # cursor = connection.cursor()
        #
        # insert_query = "INSERT INTO items VALUES(?, ?)"
        # cursor.execute(insert_query, (self.name, self.price))
        #
        # connection.commit()  # need to commit!
        # connection.close()

        # SQLAlchemy class(instance) object with properties(self.name, self.price) -transformed to- row in db
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
