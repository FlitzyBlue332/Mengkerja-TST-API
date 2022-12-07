from pydantic import BaseModel, Field, EmailStr

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
