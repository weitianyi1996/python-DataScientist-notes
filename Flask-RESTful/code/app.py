from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)   # no need different endpoints/routes


#  resource- can also be understood backend
class Student(Resource):
    # @app.route("/student/<string:name>")
    def get(self, name):
        return {"student": name}


# endpoint
api.add_resource(Student, "/student/<string:name>")  # call API- decorator  http://127.0.0.1:5000/student/toby


app.run(port=5000)



