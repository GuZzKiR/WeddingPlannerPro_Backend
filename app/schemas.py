from pydantic import BaseModel

class UserCreate(BaseModel):
    telegram_id: int
    full_name: str

class UserOut(BaseModel):
    id: int
    telegram_id: int
    full_name: str

    class Config:
        orm_mode = True