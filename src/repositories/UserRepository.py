from models.User import UserInDB, User

fake_users_db = {
    "johndoe": {
        "username": "johndoe",
        "full_name": "John Doe",
        "email": "johndoe@example.com",
        "hashed_password": "$2b$12$EixZaYVK1fsbw1ZfbX3OXePaWxn96p36WQoeG6Lruj3vjPGga31lW",
        "disabled": False,
    }
}


def get_user(username: str):
    if username in fake_users_db:
        user_dict = fake_users_db[username]
        return UserInDB(**user_dict)
    

def create_user(username: str, password: str) -> User:
    fake_users_db[username] = {
        "username": username,
        "hashed_password": password,
        "disabled": False,
    }
    return User(**fake_users_db[username])