from sqlmodel import Field, Session, SQLModel, create_engine, select
from models import Train_data


engine = create_engine("sqlite:///database.db")
s = Session(engine)


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