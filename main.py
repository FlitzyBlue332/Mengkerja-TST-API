import uvicorn
from fastapi import FastAPI, Body, Depends, HTTPException, status

from app.models import DataSchema, UserSchema, UserLoginSchema
from app.auth.auth_bearer import JWTBearer
from app.auth.auth_handler import signJWT

posts = [
    {
        "id": 1,
        "title": "Penguins ",
        "text": "Penguins are a group of aquatic flightless birds."
    },
    {
        "id": 2,
        "title": "Tigers ",
        "text": "Tigers are the largest living cat species and a memeber of the genus panthera."
    },
    {
        "id": 3,
        "title": "Koalas ",
        "text": "Koala is arboreal herbivorous maruspial native to Australia."
    },
]

users = [
    UserSchema(username= "FlitzyBlue332", email="FlitzyBlue332@sugarmail.com", password="Minut200130")
]

app = FastAPI()



def check_user(data: UserLoginSchema):
    for user in users:
        if user.email == data.email and user.password == data.password:
            return True
    return False

def check_email(data: UserLoginSchema):
    for user in users:
        if user.email == data.email:
            return True
    return False

def check_username(data: UserLoginSchema):
    for user in users:
        if user.username == data.username:
            return True
    return False

# route handlers

# testing
@app.get("/")
def greet():
    return {"Administrator": "Welcome to mein API!!"}


# Get datas
@app.get("/posts", tags=["posts"])
def get_posts():
    return { "data": posts }


@app.get("/posts/{id}", tags=["posts"])
def get_single_post(id: int):
    if id > len(posts):
        return {
            "error": "No such post with the supplied ID."
        }

    for post in posts:
        if post["id"] == id:
            return {
                "data": post
            }


@app.post("/posts", dependencies=[Depends(JWTBearer())], tags=["posts"])
def add_post(post: DataSchema):
    post.id = len(posts) + 1
    posts.append(post.dict())
    return {
        "data": "post added."
    }


@app.post("/user/signup", dependencies=[Depends(JWTBearer())], tags=["user"])
def create_user(user: UserSchema = Body(...)):
    if(check_email(user)):
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="email already exists")
    if(check_username(user)):
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="username already exists")
    users.append(user) # replace with db call, making sure to hash the password first
    return signJWT(user.email)


@app.post("/user/login", tags=["user"])
def user_login(user: UserLoginSchema = Body(...)):
    if check_user(user):
        return signJWT(user.email)
    return {
        "error": "Kesalahan login! password salah atau tidak terdapat user dengan email tersebut!"
    }

if __name__ == '__main__':
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)