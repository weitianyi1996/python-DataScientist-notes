from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)   # no need different endpoints/routes

items = []


#  resource- can also be understood backend
class Item(Resource):
    # @app.route("/student/<string:name>")
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

        data = request.get_json()  # this is user input
        item = {
                "name": name,
                "price": data["price"]
                }
        items.append(item)
        return item, 201  # 201 creating status


class ItemList(Resource):
    def get(self):
        return {"items": items}


# endpoint
api.add_resource(Item, "/item/<string:name>")  # call API- decorator  http://127.0.0.1:5000/student/toby
api.add_resource(ItemList, "/items")  # call API- decorator  http://127.0.0.1:5000/student/toby


app.run(port=5000, debug=True)



