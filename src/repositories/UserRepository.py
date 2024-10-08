from models.User import UserInDB
from models.model import User
from repositories.config import db_dependency
from uuid import uuid4

def get_user(username: str, db) -> UserInDB:
    user = db.query(User).filter(User.username == username).first()
    if user:
        print(user)
        return UserInDB(username=user.username, hashed_password=user.hashed_password, disabled=user.disabled, id=user.id) 
    

def create_user(username: str, password: str, db) -> User:
    new_user = User(username=username, hashed_password=password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user