from flask import Flask, jsonify, request, render_template

app = Flask(__name__)

stores = [
    {
        "name": "ShakeShack",
        "items": [
            {
                "name": "ShackBurger",
                "price": 5.99
            }
        ]
    }
]

# structure: JavaScript(UI)-REST API(GET/POST)-Python Backend(Calculation)
# REST API- how a web server responds to your requests(you could imagine server as a waiter)

# use Postman to test REST API:
# GET/POST request test: -like using JavaScript to create json content(input) then call REST API(endpoints)-check return


@app.route("/")  # end point
def home():
    return render_template("index-1.html")

# server
# POST - receive data
# GET - send data back
# PUT -create a new item or modify existing item


# create API endpoints example-different endpoints serve for different purpose
# jsonify-convert python dict to json(adding "")

# POST /store data: {name: } - create a new store with a given name(from browser/user)
@app.route("/store", methods=['POST'])
def create_store():
    request_data = request.get_json()  # convert json(input from user) into python dict
    new_store = {
        "name": request_data["name"],
        "items": []
    }
    stores.append(new_store)
    return jsonify(new_store)


# GET /store/<string:name> - send a specific store's info back
@app.route("/store/<string:name>", methods=["GET"])  # "http://127.0.0.1:5000/store/popeyes"
def get_store(name):
    for store in stores:
        if store["name"] == name:
            return jsonify(store)
    return jsonify({"message": "this store not found."})


# GET /store - send a list of all the stores back
@app.route("/store", methods=["GET"])
def get_all_store():
    return jsonify({"stores": stores})  # backend is the stores-dict-json(txt)-send to user


# POST /store/<string:name>/item{name:, price:} - create an item inside a specific store
@app.route("/store/<string:name>/item", methods=["POST"])
def create_item_in_store(name):
    request_data = request.get_json()  # input json- python dictionary
    for store in stores:
        if store["name"] == name:
            new_item = {
                "name": request_data["name"],
                "price": request_data["price"]
            }
            store["items"].append(new_item)
            return jsonify(store)
    return jsonify({"message": "this store not found."})


# GET /store/<string:name>/item - get all the items in a specific store
@app.route("/store/<string:name>/item", methods=["GET"])
def get_items_in_store(name):
    for store in stores:
        if store["name"] == name:
            return jsonify(store["items"])
    return jsonify({"message": "this store not found."})


# @app.route("/")  # end point
# def home():
#     return "Hello, world!"

app.run(port=5000)