from sqlalchemy.orm import Session
from app.models.user import User
from app.core.security import hash_password

def get_user_by_email(db: Session, email: str):
    return db.query(User).filter(User.email == email).first()

def create_user(db: Session, email: str, password: str, is_admin:bool = False):
    user = User(
        email=email,
        hashed_password=hash_password(password),
        is_admin=is_admin  
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    return user