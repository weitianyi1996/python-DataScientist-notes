import sqlite3


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




