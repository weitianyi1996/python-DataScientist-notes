from flask import Flask, jsonify, request

app = Flask(__name__)

stores = [
    {
        "name": "Shake Shack",
        "items": [
            {
                "name": "Shack Burger",
                "price": 5.99
            }
        ]
    }
]

# REST API- how a web server responds to your requests

# server
# POST - receive data
# GET - send data back


# create endpoints example:
# POST /store data: {name: } - create a new store with a given name(from browser/user)
@app.route("/store", methods=['POST'])
def create_store():
    request_data = request.get_json()  # convert json(input from user) into python dict
    new_store = {
        "name": request_data["name"],
        "item":[]
    }
    stores.append(new_store)
    return jsonify(new_store)


# GET /store/<string:name> - send a specific store's info back
@app.route("/store/<string:name>", methods=["GET"])  # "http://127.0.0.1:5000/store/popeyes"
def get_store(name):
    pass


# GET /store - send a list of all the stores back
@app.route("/store", methods=["GET"])
def get_all_store():
    return jsonify({"stores": stores})  # backend is the stores-dict-json(txt)-send to user


# POST /store/<string:name>/item{name:, price:} - create an item inside a specific store
@app.route("/store/<string:name>/item", methods=["POST"])
def create_item_in_store():
    pass


# GET /store/<string:name>/item - get all the items in a specific store
@app.route("/store/<string:name>/item", methods=["GET"])
def get_items_in_store():
    pass


@app.route("/")  # end point
def home():
    return "Hello, world!"

app.run(port=5000)