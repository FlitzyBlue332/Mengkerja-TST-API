from sklearn.naive_bayes import GaussianNB
from database import database
from models import Data_Predict, User_Train_data


def predict(data:Data_Predict):
    '''
    make a GNB then predict the data
    '''

    # initiate gnb classifier
    datas = database.arrayTrain()
    datas_X = datas['x']
    datas_Y = datas['y']
    gnb_classifier = GaussianNB()
    gnb_classifier.fit(datas_X, datas_Y)

    # data preprocessing
    if(data.income == "low"):
        income = 0
    else:
        income = 1
    student = int(data.student)
    lv = int(data.likes_vtuber)
    la = int(data.likes_anime)
    lm = int(data.likes_manga)
    return gnb_classifier.predict([[income,student,lv,la,lm]])






# class GNB():
#     '''
#     kelas yang ada gnb classifiernya
#     '''
#     def __init__(self):
#         datas = database.arrayTrain()
#         datas_X = datas['x']
#         datas_Y = datas['y']
#         self.gnb_classifier = GaussianNB()
#         self.gnb_classifier.fit(datas_X, datas_Y)

#     def single_fit(self,data:User_Train_data):
#         samplex = []
#         samplex.append(int(data.student))
#         samplex.append(int(data.likes_vtuber))
#         samplex.append(int(data.likes_anime))
#         samplex.append(int(data.likes_manga))
#         sampey = int(data.buys_product)
#         self.gnb_classifier.partial_fit([samplex],[sampey])

#     def predict(self, data:Data_Predict):
#         income = 0 if(data.income == "low") else 1
#         student = int(data.student)
#         lv = int(data.likes_vtuber)
#         la = int(data.likes_anime)
#         lm = int(data.likes_manga)
#         return self.gnb_classifier.predict([[income,student,lv,la,lm]])