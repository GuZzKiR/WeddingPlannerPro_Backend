from fastapi import APIRouter
from app.schemas import UserCreate, UserOut
from app.models import User
from app.database import SessionLocal
from sqlalchemy.orm import Session

router = APIRouter(prefix="/users", tags=["Users"])

@router.post("/", response_model=UserOut)
def register_user(user: UserCreate):
    db: Session = SessionLocal()
    existing = db.query(User).filter(User.telegram_id == user.telegram_id).first()
    if existing:
        return existing
    new_user = User(telegram_id=user.telegram_id, full_name=user.full_name)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user