from db import db
# 1 item belong to 1 store, 1 store has many items


class StoreModel(db.Model):
    __tablename__ = "stores"

    # 3 columns SQLAlchemt must match instance properties(self.id, username, password)
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))

    items = db.relationship("ItemModel")  # this is a list, tell SQLAlchemy there is relationship between these two (tables)

    def __init__(self, name):  # later be used either inserted or updated to database
        self.name = name

    def json(self):
        return {"name": self.name, "items": [item.json() for item in self.items]}

    @classmethod
    def find_by_name(cls, name):  # !this is going to return an object
        # using SQLAlchemy-difference: SQLite using SQL(SELECT*FROM A), SQLAlchemy using query/filter...
        # return an ItemModel object(because of cls)
        # row in db -transformed to- class object with properties(self.name, self.price)
        item_json = cls.query.filter_by(name=name).first().json()  # SELECT*FROM items WHERE name=name LIMIT 1
        return {"item": item_json}

    def save_to_db(self):  # !this is not going to return anything-create object instance-item.insert()
        # SQLAlchemy class(instance) object with properties(self.name, self.price) -transformed to- row in db
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
