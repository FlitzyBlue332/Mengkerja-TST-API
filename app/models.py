from pydantic import BaseModel, Field, EmailStr
from sqlmodel import SQLModel
from typing import Optional

class DataSchema(BaseModel):
    id: int = Field(default=None)
    title: str = Field(...)
    content: str = Field(...)

    class Config:
        schema_extra = {
            "example": {
                "title": "Sugar",
                "content": "Wangy Wangy Wangy Wangy"
            }
        }

class Train_data(SQLModel, table=True):
    '''
    isi database adalah:  
    id: int
    income: str
    student: bool
    likes_vtuber: bool
    likes_anime: bool
    likes_manga: bool
    buys_product: bool
    '''
    id: Optional[int] = Field(default=None, primary_key=True)
    income: str
    student: bool
    likes_vtuber: bool
    likes_anime: bool
    likes_manga: bool
    buys_product: bool

class Data_Predict(BaseModel):
    income: str = Field(...)
    student: bool = Field(...)
    likes_vtuber: bool = Field(...)
    likes_anime: bool = Field(...)
    likes_manga: bool = Field(...)

class User_Train_data(BaseModel):
    student: bool = Field(...)
    likes_vtuber: bool = Field(...)
    likes_anime: bool = Field(...)
    likes_manga: bool = Field(...)
    buys_product: bool = Field(...)

class UserSchema(BaseModel):
    username: str = Field(...)
    email: EmailStr = Field(...)
    password: str = Field(...)

    class Config:
        schema_extra = {
            "example": {
                "username": "FlitzyBlue332",
                "email": "FlitzyBlue332@sugarmail.com",
                "password": "Minut200130"
            }
        }

class UserLoginSchema(BaseModel):
    email: EmailStr = Field(...)
    password: str = Field(...)

    class Config:
        schema_extra = {
            "example": {
                "email": "FlitzyBlue332@sugarmail.com",
                "password": "Minut200130"
            }
        }
