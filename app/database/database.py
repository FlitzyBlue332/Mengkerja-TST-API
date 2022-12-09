from typing import Optional
from sqlmodel import Field, Session, SQLModel, create_engine, select
from models import User_Train_data


engine = create_engine("sqlite:///database.db")
s = Session(engine)

# kelas khusus database
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


# untuk classification
def getalldata():
    '''
    ambil semua data pada tabel train
    '''
    statement = select(Train_data)
    datas = s.exec(statement).all()
    return datas

def arrayTrain():
    '''
    isinya ngga class, langsung fit ke model aja
    '''
    datas_X = []
    datas_Y = []
    #income, student, likes_vtuber, likes_anime, likes_manga, buys_product
    predatas = getalldata()
    for data in predatas:
        sample = []

        # handling categorical income
        if(data.income == "low"):
            # income low -> income = 0
            sample.append(0)
        else:
            sample.append(1)
        sample.append(int(data.student))
        sample.append(int(data.likes_vtuber))
        sample.append(int(data.likes_anime))
        sample.append(int(data.likes_manga))
        datas_Y.append(int(data.buys_product))
        datas_X.append(sample)
    datas = {'x' : datas_X, 'y' : datas_Y}
    return datas


# insert data
def insertData(data:User_Train_data):
    sample = Train_data(
        income= data.income,
        student= data.student,
        likes_vtuber= data.likes_vtuber,
        likes_anime= data.likes_anime,
        likes_manga= data.likes_manga,
        buys_product= data.buys_product
    )
    s.add(sample)
    s.commit()

def checkInsertData(data:User_Train_data):
    '''
    kalau true berarti aman di insert
    '''
    return data.income == 'high' or data.income == 'low'