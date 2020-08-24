from flask_restful import Resource

from models.store import StoreModel

# items = []  # mimic in memory database-replaced by sqlite database


#  resource- can also be understood backend
class Store(Resource):
    # request parsing- check the input(JSON payload) is correct-missing needed key
    # saved this input as class variable so can be used anywhere

    # @app.route("/student/<string:name>")
    def get(self, name):
        # item = next(filter(lambda item: item["name"] == name, items), None)  # return True/False- if no value return None
        store = StoreModel.find_by_name(name)
        if store:
            return store.json()
        return {"message": "This store has not been found!"}, 404

    def post(self, name):
        # send item to server and give it a price from UI

        # if next(filter(lambda item: item["name"] == name, items), None):  # check if this item already exist
        #     return "this {} already exist.".format(name), 400
        if StoreModel.find_by_name(name):
            return "this {} already exist.".format(name), 400

        store = StoreModel(name)

        try:
            store.save_to_db()
        except:
            return {"message": " NOTICE! An error occurred while inserting!"}, 500  # Internal Server Error

        return store.json(), 201  # 201 creating status

    def delete(self, name):
        # global items  # otherwise will be local variable and cant use variable to define itself
        # items = list(filter(lambda item: item["name"] != name, items))

        store = StoreModel.find_by_name(name)
        if store:
            store.delete_from_db()

        return {"message": "GREAT! Store has been deleted."}


class StoreList(Resource):
    def get(self):
        return {"stores": [store.json() for store in StoreModel.query.all()]}  # item already in class instance object