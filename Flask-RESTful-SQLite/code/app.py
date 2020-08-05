from flask import Flask, request
from flask_restful import Resource, Api, reqparse
from flask_jwt import JWT, jwt_required

from security import authenticate, identity
from user import UserRegister

app = Flask(__name__)
app.secret_key = "tianyi"
api = Api(app)   # no need different endpoints/routes

jwt = JWT(app, authenticate, identity)  # jwt object create a new endpoint: /auth
# auth workflow: if authenticate function pass return jw token-- pass to identity function
# jwt_required() done- call GET/POST method

items = []  # mimic in memory database


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
        # for item in items:
        #     if item["name"] == name:
        #         return item  # no jsonify needed for flask_restful

        item = next(filter(lambda item: item["name"] == name, items), None)  # return True/False- if no value return None
        # return map(lambda item: return item if item["name"] == name, items)  # filter-map

        # should return a json format thing-most popular http status code is 200
        return {"item": item}, 200 if item else 404

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


# endpoint
api.add_resource(Item, "/item/<string:name>")  # call API- decorator  http://127.0.0.1:5000/student/toby
api.add_resource(ItemList, "/items")  # call API- decorator  http://127.0.0.1:5000/student/toby
api.add_resource(UserRegister, "/register")  # call API- decorator  http://127.0.0.1:5000/register


app.run(port=8000, debug=True)



