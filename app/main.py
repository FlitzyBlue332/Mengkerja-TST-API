import uvicorn
from fastapi import FastAPI, Body, Depends, HTTPException, status

from models import UserSchema, UserLoginSchema, Data_Predict, User_Train_data
from auth.auth_bearer import JWTBearer
from auth.auth_handler import signJWT
import classification
from database import database


app = FastAPI()

def check_user(data: UserLoginSchema):
    users = database.getUser()
    for user in users:
        if user.email == data.email and user.password == data.password:
            return True
    return False

def check_email(data):
    users = database.getUser()
    for user in users:
        if user.email == data.email:
            return True
    return False

def check_username(data):
    users = database.getUser()
    for user in users:
        if user.username == data.username:
            return True
    return False




# route handlers

# testing
@app.get("/")
def greet():
    return {"Administrator": "Welcome to mein API!!"}

# prediction
@app.post("/classify/predict", tags=["classification"])
def prediction(data: Data_Predict = Body(...)):
    result = classification.predict(data)
    if(result == 1):
        return {"Hasil Prediksi":"Membeli"}
    else:
        return {"Hasil Prediksi":"Tidak Membeli"}



# Add training data
@app.post("/classify/train_data", dependencies=[Depends(JWTBearer())], tags=["classification"])
def addTrainingData(data: User_Train_data = Body(...)):
    if(database.checkInsertData):
        database.insertClassiData(data)
        return {"message":"insert berhasil dilakukan"}
    else:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="income value must be 'low' or 'high'")
    
# Get datas
@app.get("/classify/get_data", tags=["classification"])
def get_train_data():
    datas = database.getalldata()
    return datas


@app.post("/user/signup", dependencies=[Depends(JWTBearer())], tags=["user"])
def create_user(user: UserSchema = Body(...)):
    if(check_email(user)):
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="email already exists")
    if(check_username(user)):
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="username already exists")
    database.insertUser(user)
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