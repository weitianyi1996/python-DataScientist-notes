from user import User

users = [
    User(1, "Toby", "password123")
]

username_mapping = {u.username: u for u in users}
userid_mapping = {u.id: u for u in users}


def authenticate(username, password):
    user = username_mapping.get(username, None)
    if user and user.password == password:
        return user


def identity(payload):
    user_id = payload["identity"]  # use return JW token to get user id
    return userid_mapping.get(user_id, None)


