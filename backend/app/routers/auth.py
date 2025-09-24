from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from ..database import get_db
from ..models.user import User
from ..security import verify_password, create_access_token, get_password_hash


router = APIRouter()


@router.post("/login")
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = db.query(User).filter(User.email == form_data.username).first()
    if not user or not verify_password(form_data.password, user.hashed_password):
        raise HTTPException(status_code=400, detail="Incorrect email or password")
    return {"access_token": create_access_token(user.email), "token_type": "bearer"}


@router.post("/register")
def register(email: str, password: str, db: Session = Depends(get_db)):
    existing = db.query(User).filter(User.email == email).first()
    if existing:
        raise HTTPException(status_code=400, detail="Email already registered")
    user = User(email=email, hashed_password=get_password_hash(password), role="organizer")
    db.add(user)
    db.commit()
    db.refresh(user)
    return {"id": user.id, "email": user.email}

