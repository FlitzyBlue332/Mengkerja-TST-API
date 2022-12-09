from pydantic import BaseModel, Field, EmailStr
from sqlmodel import SQLModel
from typing import Optional


class Data_Predict(BaseModel):
    income: str = Field(...)
    student: bool = Field(...)
    likes_vtuber: bool = Field(...)
    likes_anime: bool = Field(...)
    likes_manga: bool = Field(...)

    class Config:
        schema_extra = {
            "example": {
                "income": "low",
                "student": "true",
                "likes_vtuber": "true",
                "likes_anime": "true",
                "likes_manga": "true"
            }
        }

class User_Train_data(BaseModel):
    income: str = Field(...)
    student: bool = Field(...)
    likes_vtuber: bool = Field(...)
    likes_anime: bool = Field(...)
    likes_manga: bool = Field(...)
    buys_product: bool = Field(...)

    class Config:
        schema_extra = {
            "example": {
                "income": "low",
                "student": "true",
                "likes_vtuber": "true",
                "likes_anime": "true",
                "likes_manga": "true",
                "buys_product": "true"
            }
        }

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
