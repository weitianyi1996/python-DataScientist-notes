from flask import Flask, request
import sqlite3
from flask_restful import Resource,  reqparse
from flask_jwt import jwt_required

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

        connection = sqlite3.connect("data.db")
        cursor = connection.cursor()

        query = "SELECT * FROM items WHERE name=?"
        result = cursor.execute(query, (name,))
        row = result.fetchone()

        connection.close()

        if row:
            return {"item":{"name": row[0], "price": row[1]}}
        return {"message":"item not found"}, 404

    def post(self, name):
        # send item to server and give it a price from UI

        if next(filter(lambda item: item["name"] == name, items), None):  # check if this item already exist
            return "this {} already exist.".format(name), 400

        data = Item.parser.parse_args()
        # data = request.get_json()  # this is user input
        item = {
                "name": name,
                "price": data["price"]
                }
        items.append(item)
        return item, 201  # 201 creating status

    def delete(self, name):
        global items  # otherwise will be local variable and cant use variable to define itself
        items = list(filter(lambda item: item["name"] != name, items))

        return {"message": "item has been deleted."}

    def put(self, name):

        # data = request.get_json()
        data = Item.parser.parse_args()  # input

        for item in items:
            if item["name"] == name:
                item.update(data)
                return item
        item = {
            "name": name,
            "price": data["price"]
        }
        items.append(item)
        return item


class ItemList(Resource):
    def get(self):
        return {"items": items}