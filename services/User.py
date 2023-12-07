from Repository.User import create_user_repository, get_users_repository, update_user_repository, delete_user_repository, authenticate_user_repository
from models.User import User


def create_user(user: User):
    name = user.name
    password = user.password
    email = user.email


    return create_user_repository(name, password, email)

def get_users():
    return get_users_repository()

def update_user(id: int, user: User):
    return update_user_repository(id, user)

def delete_user(id: int):
    return delete_user_repository(id)

def authenticate_user(username: str, password: str):
    return authenticate_user_repository(username, password)