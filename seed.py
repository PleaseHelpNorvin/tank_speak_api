# seed.py
from sqlalchemy.orm import Session
from app.db.base import engine
from app.models.user import User
from app.core.security import hash_password  # import your password hasher

session = Session(bind=engine)

users_to_seed = [
    User(email="admin@example.com", hashed_password=hash_password("admin123")),
    User(email="user1@example.com", hashed_password=hash_password("user123")),
]

# Avoid duplicates
for u in users_to_seed:
    if not session.query(User).filter_by(email=u.email).first():
        session.add(u)

session.commit()
session.close()
print("Seeding complete!")