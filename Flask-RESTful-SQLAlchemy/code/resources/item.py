from flask import Flask, request
import sqlite3
from flask_restful import Resource,  reqparse
from flask_jwt import jwt_required

from models.item import ItemModel

# items = []  # mimic in memory database-replaced by sqlite database


#  resource- can also be understood backend
class Item(Resource):
    # request parsing- check the input(JSON payload) is correct-missing needed key
    # saved this input as class variable so can be used anywhere
    parser = reqparse.RequestParser()
    parser.add_argument("price",  # check if include "price" in dict's key
                        type=float,
                        required=True,
                        help="Check input! This field can not leave blank!!!"
                        )

    # @app.route("/student/<string:name>")
    @jwt_required()  # jwt auth before calling GET method
    def get(self, name):
        # item = next(filter(lambda item: item["name"] == name, items), None)  # return True/False- if no value return None
        item = ItemModel.find_by_name(name)
        if item:
            return item
        return {"message": "item not found"}, 404

    def post(self, name):
        # send item to server and give it a price from UI

        # if next(filter(lambda item: item["name"] == name, items), None):  # check if this item already exist
        #     return "this {} already exist.".format(name), 400
        if ItemModel.find_by_name(name):
            return "this {} already exist.".format(name), 400

        data = Item.parser.parse_args()
        item = ItemModel(name=name, price=data["price"])

        try:
            item.save_to_db()
        except:
            return {"message": " NOTICE! An error occurred while inserting!"}, 500  # Internal Server Error

        return item, 201  # 201 creating status

    def delete(self, name):
        # global items  # otherwise will be local variable and cant use variable to define itself
        # items = list(filter(lambda item: item["name"] != name, items))

        item = ItemModel.find_by_name(name)
        if item:
            item.delete_from_db()

        return {"message": "GREAT! Item has been deleted."}

    # if exist update, or add new item
    def put(self, name):
        data = Item.parser.parse_args()  # input

        item = Item.find_by_name(name)

        if item:
            item["price"] = data["price"]  # update it
        else:
            item = ItemModel(name=name, price=data["price"])

        item.save_to_db()  # update or insert(class/zinstance object with properties into db row)

        return item.json()


class ItemList(Resource):
    def get(self):
        # connection = sqlite3.connect("data.db")
        # cursor = connection.cursor()
        #
        # query = "SELECT * FROM items"
        # result = cursor.execute(query)
        #
        # items = []
        # for row in result:
        #     items.append({
        #         "name": row[0],
        #         "price": row[1]
        #     })
        #
        # # connection.commit()  # need to commit! when editing datatable
        # connection.close()

        return {"items": [item.json() for item in ItemModel.query.all()]}  # item already in class instance object