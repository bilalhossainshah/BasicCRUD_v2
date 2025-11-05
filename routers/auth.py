

   
# import secrets
# from fastapi import Depends,FastAPI,HTTPException,status,APIRouter
# from sqlalchemy.orm import Session
# from passlib.context import CryptContext
# from jose import JWTError,jwt
# from datetime import datetime, timedelta
# from pydantic import BaseModel

# from models import User
# from database import SessionLocal

# SECRET_KEY = "lalallalalal"
# ALGORITHM = "HS256"
# ACCESS_TOKEN_EXPIRE_MINUTES = 60

# pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
# router = APIRouter(prefix="/auth", tags=["Auth"])

# def get_db():
#     db = SessionLocal()
#     try:
#         yield db
    
#     finally:
#         db.close()

# def hash_password(password: str):
#     password = str(password)
#     print("🔍 Password before hashing:", password, " | Length:", len(password))

#     return pwd_context.hash(password)

# def verify_password(plain_password, hashed_password):
#     return pwd_context.verify(plain_password, hashed_password)

# def create_access_token(data:dict, expires_delta : timedelta | None= None):
#     to_encode = data.copy()
#     expire = datetime.utcnow() + (expires_delta or timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES))
#     to_encode.update({"exp": expire})
#     return jwt.encode(to_encode,SECRET_KEY,algorithm=ALGORITHM)

# class UserRegister(BaseModel):
#     email: str
#     password: str
    
# class UserLogin(BaseModel):
#     email: str
#     password: str


# @router.post("/register")
# def register_user(user:UserRegister, db:Session = Depends(get_db)):
#     existing_user = db.query(User).filter(User.email == user.email).first()
#     if existing_user:
#         raise HTTPException(status_code=400,detail="User Already Registered")
    
#     hashed_pw = hash_password(user.password)
#     new_user = User(email = user.email, password=hashed_pw)
#     db.add(new_user)
#     db.commit()
#     db.refresh(new_user)
#     return {"message": "User Registered Successfully"}

# @router.post("/login")
# def login_user(user:UserLogin,db:Session = Depends(get_db)):
#     db_user = db.query(User).filter(User.email == user.email).first()
#     if not db_user or not verify_password(user.password,db_user.password):
#         raise HTTPException(status_code=402,detail="Invalid Credentials")
#     access_token = create_access_token({"sub": db_user.email})
#     return {"access_token":access_token,"token_type":"bearer"}
import os, hashlib
from fastapi import APIRouter
from database import get_conn

router = APIRouter(prefix="/auth", tags=["Auth"])

@router.post("/register")
def register_user(username: str, password: str):
    conn = get_conn()
    cursor = conn.cursor()

    salt = os.urandom(16)
    hashed_pw = hashlib.sha256(salt + password.encode()).hexdigest()

    cursor.execute("INSERT INTO Users (username, salt, password) VALUES (?, ?, ?)",
                   (username, salt.hex(), hashed_pw))
    conn.commit()
    conn.close()
    return {"message": "User Added Successfully"}


@router.post("/login")
def login(username: str, password: str):
    conn = get_conn()
    cursor = conn.cursor()
    cursor.execute("SELECT salt, password FROM Users WHERE username = ?", (username,))
    result = cursor.fetchone()
    conn.close()

    if not result:
        return {"message": "User Doesn't Exist"}

    salt_hex, stored_password = result
    salt = bytes.fromhex(salt_hex)  
    hashed_input = hashlib.sha256(salt + password.encode()).hexdigest()

    if hashed_input == stored_password:
        return {"message": "Login Successful"}
    else:
        return {"message": "Invalid Credentials"}
