from models.user import UserModel

users = [
    UserModel(1, "Toby", "password123")
]

username_mapping = {u.username: u for u in users}
userid_mapping = {u.id: u for u in users}


def authenticate(username, password):
    user = UserModel.find_by_username(username)  # create user instance using sql data
    if user and user.password == password:
        return user


def identity(payload):
    user_id = payload["identity"]  # use return JW token to get user id, check if JWT token is correct
    return UserModel.find_by_userid(user_id)


