from passlib.context import CryptContext
from jose import jwt
from datetime import datetime, timedelta
import hashlib

SECRET_KEY = "your-secret-key"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60



def hash_password(password: str):
    # simple MD5 hash (insecure!)
    return hashlib.md5(password.encode("utf-8")).hexdigest()

def verify_password(plain: str, hashed: str):
    return hashlib.md5(plain.encode("utf-8")).hexdigest() == hashed

def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)