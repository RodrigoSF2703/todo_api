from pydantic import BaseModel

class UserBase(BaseModel):
    username: str

class UserCreate(UserBase):
    token: str

class User(UserBase):
    id: int

    class Config:
        orm_mode = True