from sqlalchemy.orm import Session
from models import User

def create_user(db: Session, name: str):
    """
    Create a new user.
    """
    new_user = User(name=name)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

def get_user_by_id(db: Session, user_id: int):
    """
    Retrieve a user by their ID.
    """
    return db.query(User).filter(User.id == user_id).first()

def update_user_name(db: Session, user_id: int, new_name: str):
    """
    Update a user's name by their ID.
    """
    user = db.query(User).filter(User.id == user_id).first()
    if user:
        user.name = new_name
        db.commit()
        db.refresh(user)
    return user

def delete_user(db: Session, user_id: int):
    """
    Delete a user by their ID.
    """
    user = db.query(User).filter(User.id == user_id).first()
    if user:
        db.delete(user)
        db.commit()
    return user
