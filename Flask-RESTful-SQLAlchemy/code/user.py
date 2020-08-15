import sqlite3
from flask_restful import Resource, reqparse


class User:
    def __init__(self, _id, username, password):
        self.id = _id
        self.username = username
        self.password = password

    @classmethod  # create a special class instance
    # search input username at the sql database
    def find_by_username(cls, username):
        connection = sqlite3.connect("data.db")
        cursor = connection.cursor()

        select_query = "SELECT* FROM users WHERE username=?"
        result = cursor.execute(select_query, (username, ))
        row = result.fetchone()
        if row:
            user = cls(row[0], row[1], row[2])
        else:
            user = None

        connection.close()
        return user

    @classmethod  # create a special class instance
    # search input username at the sql database
    def find_by_userid(cls, userid):
        connection = sqlite3.connect("data.db")
        cursor = connection.cursor()

        select_query = "SELECT* FROM users WHERE id=?"
        result = cursor.execute(select_query, (userid, ))
        row = result.fetchone()
        if row:
            user = cls(row[0], row[1], row[2])
        else:
            user = None

        connection.close()
        return user


# let a user to sign up(later will create a new endpoint)
class UserRegister(Resource):
    # user input in web/payload
    parser = reqparse.RequestParser()
    parser.add_argument("username",  # check if include "username" in dict's key
                        type=str,
                        required=True,
                        help="Check input! This field can not leave blank!!!"
                        )
    parser.add_argument("password",
                        type=str,
                        required=True,
                        help="Check input! This field can not leave blank!!!"
                        )

    def post(self):
        data = UserRegister.parser.parse_args()

        # avoid duplicate username
        if User.find_by_username(data["username"]):
            return {"message": "user already exist, please input a new username"}, 400

        connection = sqlite3.connect("data.db")
        cursor = connection.cursor()

        # insert values
        insert_query = "INSERT INTO users VALUES(NULL, ?, ?)"
        cursor.execute(insert_query, (data["username"], data["password"]))

        connection.commit()
        connection.close()

        return {"message": "GREAT! User has been signed up."}




