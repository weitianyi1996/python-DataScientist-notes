from flask import Flask
from flask_restful import Api
from flask_jwt import JWT

from security import authenticate, identity
from user import UserRegister

from item import Item, ItemList

app = Flask(__name__)
app.secret_key = "tianyi"
api = Api(app)   # no need different endpoints/routes

jwt = JWT(app, authenticate, identity)  # jwt object create a new endpoint: /auth
# auth workflow: if authenticate function pass return jw token-- pass to identity function
# jwt_required() done- call GET/POST method




# endpoint
api.add_resource(Item, "/item/<string:name>")  # call API- decorator  http://127.0.0.1:5000/student/toby
api.add_resource(ItemList, "/items")  # call API- decorator  http://127.0.0.1:5000/student/toby
api.add_resource(UserRegister, "/register")  # call API- decorator  http://127.0.0.1:5000/register


app.run(port=9000, debug=True)



