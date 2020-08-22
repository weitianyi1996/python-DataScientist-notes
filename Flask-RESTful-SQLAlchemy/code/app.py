from flask import Flask
from flask_restful import Api
from flask_jwt import JWT

from security import authenticate, identity
from resources.user import UserRegister

from resources.item import Item, ItemList

from db import db

app = Flask(__name__)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.secret_key = "tianyi"
api = Api(app)   # no need different endpoints/routes

jwt = JWT(app, authenticate, identity)  # jwt object create a new endpoint: /auth
# auth workflow: if authenticate function pass return jw token-- pass to identity function
# jwt_required() done- call GET/POST method


# endpoints
api.add_resource(Item, "/item/<string:name>")  # call API- decorator  http://127.0.0.1:5000/student/toby
api.add_resource(ItemList, "/items")  # call API- decorator  http://127.0.0.1:5000/student/toby
api.add_resource(UserRegister, "/register")  # call API- decorator  http://127.0.0.1:5000/register


# make sure it's only running app.py
# if imported by other file, __name__ = item
if __name__ == "__main__":  # check if running itself
    db.init_app(app)
    app.run(port=9000, debug=True)



